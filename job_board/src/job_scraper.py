# native imports
import re
import requests
import pickle
import hashlib
from datetime import datetime
import time
import os

# my scripts
import db
import filtering

# get connection to database
db.init_db()
conn = db.get_connection()

#file paths
DELETED_HASH_FILE = os.path.join(os.path.dirname(__file__), "..", "text", "deleted_hashes.txt")
SCRAPER_LOG_FILE = os.path.join(os.path.dirname(__file__), "..", "logging", "scraper_log.txt")
FILTER_LOG_FILE = os.path.join(os.path.dirname(__file__), "..", "logging", "filter_log.txt")

# helper functions

#get most recent job in database
def get_newest_db_job_timestamp(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(created_at) FROM jobs")
    result = cursor.fetchone()
    return result[0] if result and result[0] else 0  

#attempt to infer years of experience from title
def years_of_experience(job):
    title = job["title"].lower()
    if re.search(r"\b(president|vp)\b", title): return 20
    if re.search(r"\b(chief|principal)\b", title): return 12
    if re.search(r"\bstaff\b", title): return 8
    if re.search(r"\b(manager|lead)\b", title): return 6
    if re.search(r"\b(senior|sr\.?)\b", title): return 5
    if re.search(r"\b(mid|mid-level|midlevel|mid level)\b", title): return 2
    if re.search(r"\b(junior|entry|jr\.?)\b", title): return 0
    if re.search(r"\b(associate|assoc\.?)\b", title): return 0
    if re.search(r"\b(graduate|grad\.?)\b", title): return 0
    if re.search(r"\b(early career|early-career)\b", title): return 0
    return 2

#convert time
def iso_to_ts(created_str):
    return int(datetime.fromisoformat(created_str.replace("Z","+00:00")).timestamp())

#get hash of job for deduplication purposes
def job_hash(title, description):
    text = (title + description[:300]).lower().strip()
    return hashlib.sha1(text.encode()).hexdigest()

#get existing hashes in database
def get_existing_hashes(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT content_hash FROM jobs")
    return {row[0] for row in cursor.fetchall()}

#get deleted hashes
def get_deleted_hashes():
    if not os.path.exists(DELETED_HASH_FILE):
        return set()
    with open(DELETED_HASH_FILE, "r") as f:
        return {line.strip() for line in f.readlines()}

#add deleted hashes to text file
def add_deleted_hash(h):
    with open(DELETED_HASH_FILE, "a") as f:
        f.write(h + "\n")

#get information from individual job dictionary
def get_entries(job, category):
    yoe = years_of_experience(job)
    content_hash = job_hash(job["title"], job["description"])
    salary_min = job.get("salary_min") or "Unknown"
    salary_max = job.get("salary_max") or "Unknown"
    company = job.get("company", {}).get("display_name", "Unknown") or "Unknown"
    adzuna_id = job["id"]
    url = job["redirect_url"]
    title = job["title"]
    description = job["description"]
    created_at = iso_to_ts(job["created"])
    return content_hash, adzuna_id, title, company, description, url, salary_min, salary_max, yoe, created_at, category

# main job scrape

#adzuna parameters
APP_ID = None #please enter your APP_ID
APP_KEY = None #please enter your APP_KEY
BASE_URL = "https://api.adzuna.com/v1/api/jobs/us/search/{}"
job_titles = ["machine learning engineer","software engineer","data scientist"]
calls = 0
page_limit = 80
fresh_jobs = {title:[] for title in job_titles}

#get timestamp for early stopping and hashes for deduplication
newest_ts = get_newest_db_job_timestamp(conn)
existing_hashes = get_existing_hashes(conn)
deleted_hashes = get_deleted_hashes()

#scrape loop; adheres to free api call limits
for job_title in job_titles:    
    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "results_per_page": 50,
        "what": job_title,
        "where": "US",
        "sort_by":"date"
    }
    page = 1
    
    while page <= page_limit:
        if calls>0 and calls%25==0:
            time.sleep(60)
        calls += 1
        response = requests.get(BASE_URL.format(page), params=params)
        data = response.json()
        if not data["results"]:
            break
    
        all_older = True
        for job in data["results"]:
            job_ts = iso_to_ts(job["created"])
            if job_ts > newest_ts:
                all_older = False
                fingerprint = job_hash(job["title"], job["description"])
                if fingerprint not in existing_hashes and fingerprint not in deleted_hashes:
                    fresh_jobs[job_title].append(job)
                    existing_hashes.add(fingerprint)
        if all_older:
            break
        page += 1

#positive and negative counts from filtering for logging
total_simple_positives = 0
total_simple_negatives = 0
total_bert_positives = 0
total_bert_negatives = 0

# filtering
jobs_to_add = []
for title in job_titles:
    filtered_jobs,simple_positives,simple_negatives,bert_positives,bert_negatives = filtering.sift(fresh_jobs[title])
    total_simple_positives+=simple_positives
    total_simple_negatives+=simple_negatives
    total_bert_positives+=bert_positives
    total_bert_negatives+=bert_negatives
    for job in filtered_jobs:
        jobs_to_add.append([job, title])

insertions = 0
# adding to database
for job, category in jobs_to_add:
    insertions+=1
    entry = get_entries(job, category)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO jobs (content_hash,adzuna_id,title,company,description,url,salary_min,salary_max,yoe,created_at,category)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, entry)
conn.commit()


# remove all old/experienced jobs to keep db size in bounds
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM jobs")
total = cursor.fetchone()[0]
if total > 10000:
    cursor.execute("""
        DELETE FROM jobs
        WHERE id IN (
            SELECT id FROM jobs
            ORDER BY yoe DESC, created_at ASC
            LIMIT ?
        );
    """, (total - 10000,))

#logging
end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
end_calls = str(calls)
end_insertions = str(insertions)

api_log = end_time + " " + end_calls + " " + end_insertions
filter_log = end_time+" "+str(total_simple_positives)+" "+str(total_simple_negatives)+" "+str(total_bert_positives)+" "+str(total_bert_negatives)

with open(SCRAPER_LOG_FILE, "a") as file:
    file.write(api_log + "\n")

with open(FILTER_LOG_FILE, "a") as file:
    file.write(filter_log + "\n")