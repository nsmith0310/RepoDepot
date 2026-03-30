#imports
import requests
import pickle
import time
import hashlib
import os

#hash function for deduplication
def job_hash(title, description):
    text = (title + description[:300]).lower().strip()
    return hashlib.sha1(text.encode()).hexdigest()

#get job titles to build initial dataset
file_path = os.path.join(os.path.dirname(__file__), "..", "text", "job_titles.txt")

#parse job titles into positives (relevant) and negatives (irrelevant)
positive_titles = []
negative_titles = []

positive_lines = True
with open(file_path, 'r') as file:
    for line in file:
        text = line.strip()
        if text=="":
            positive_lines=False
        else:
            if positive_lines:
                positive_titles.append(text)
            else:
                negative_titles.append(text)

#adzuna parameters
APP_ID = None #please enter your APP_ID
APP_KEY = None #please enter your APP_KEY

BASE_URL = "https://api.adzuna.com/v1/api/jobs/us/search/{}"

calls = 0
limit = 50
seen_jobs = set()

print()
print("###################################### Positive titles ######################################")
print()

#scrape jobs based on relevant titles
positives = []

for positive_job_title in positive_titles:
    
    job_list = []
    
    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "results_per_page": 50,
        "what": positive_job_title,
        "where": "US"
    }
    page = 1
    url = BASE_URL.format(page)
    
    counter = 0
    while True:
        if calls>0 and calls%25==0:
            time.sleep(60)
        calls+=1
        response = requests.get(BASE_URL.format(page), params=params)
        data = response.json()
        if not data["results"]:
            break
            
        for job in data["results"]:
            fingerprint = job_hash(job["title"], job["description"])
                
            if fingerprint not in seen_jobs:
                job_list.append(job)
                seen_jobs.add(fingerprint)
                counter+=1
                
                if counter==limit:
                    break
        if counter==limit:
            break
        else:
            page+=1
    
    positives.append([positive_job_title,job_list])
    print(positive_job_title+" DONE; jobs:"+str(counter))
    

print()
print("###################################### Negative titles ######################################")
print()

#scrape jobs based on irrelevant titles
negatives = []

for negative_job_title in negative_titles:
    
    job_list = []
    
    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "results_per_page": 50,
        "what": negative_job_title,
        "where": "US"
    }
    page = 1
    url = BASE_URL.format(page)
    
    counter = 0
    while True:
        if calls>0 and calls%25==0:
            time.sleep(60)
        calls+=1
        response = requests.get(BASE_URL.format(page), params=params)
        data = response.json()
        if not data["results"]:
            break
            
        for job in data["results"]:
            fingerprint = job_hash(job["title"], job["description"])
                
            if fingerprint not in seen_jobs:
                job_list.append(job)
                seen_jobs.add(fingerprint)
                counter+=1
                if counter==limit:
                    break
        if counter==limit:
            break
        else:
            page+=1
    
    negatives.append([negative_job_title,job_list])
    print(negative_job_title+" DONE; jobs:"+str(counter))

print()

#save the positive and negative jobs

POSITIVE_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "positive_jobs.pkl")

with open(POSITIVE_PATH, 'wb') as f:
    pickle.dump(positives, f) 

print("Positive jobs written.")

NEGATIVE_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "negative_jobs.pkl")

with open(NEGATIVE_PATH, 'wb') as f:
    pickle.dump(negatives, f)

print("Negative jobs written.")            