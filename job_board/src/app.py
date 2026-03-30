#imports
import sqlite3
from flask import Flask, render_template_string, request, redirect
import os
import json
import math

#file paths
DB_NAME = os.path.join(os.path.dirname(__file__), "..", "db", "jobs.db")
DELETED_HASH_FILE = os.path.join(os.path.dirname(__file__), "..", "text", "deleted_hashes.txt")
IRRELEVANT_JOBS_FILE = os.path.join(os.path.dirname(__file__), "..", "text", "irrelevant_jobs.jsonl")
RELEVANT_JOBS_FILE = os.path.join(os.path.dirname(__file__), "..", "text", "relevant_jobs.jsonl")
HTML_FILE = os.path.join(os.path.dirname(__file__), "..", "html", "template.html")

app = Flask(__name__)

PAGE_SIZE = 50

#track deleted jobs so as to not process later
def add_deleted_hash(h):
    with open(DELETED_HASH_FILE, "a") as f:
        f.write(h + "\n")

#track irrelevant jobs for tuning model
def add_irrelevant_job(job):
    with open(IRRELEVANT_JOBS_FILE, "a") as f:
        f.write(json.dumps(job) + "\n")

#track relevant jobs for tuning model
def add_relevant_job(job):
    with open(RELEVANT_JOBS_FILE, "a") as f:
        f.write(json.dumps(job) + "\n")

#update browser
@app.route("/", methods=["GET", "POST"])
def show_jobs():
    categories = ["machine learning engineer", "software engineer", "data scientist"]

    # Track current page per category
    pages = {}
    for cat in categories:
        pages[cat] = int(request.form.get(f"page_{cat}", 1))

    action = request.form.get("action")

    # Handle pagination clicks
    if action:
        for cat in categories:
            if action == f"next_{cat}":
                pages[cat] += 1
            elif action == f"prev_{cat}":
                pages[cat] = max(1, pages[cat] - 1)

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT content_hash, category, title, company, description, yoe, salary_min, salary_max, url, created_at
            FROM jobs
            ORDER BY yoe ASC, created_at DESC
        """)
        jobs = cursor.fetchall()

    categorized_full = {c: [] for c in categories}

    for job in jobs:
        content_hash, cat, title, company, description, yoe, sal_min, sal_max, url, _ = job
        if cat in categorized_full:
            categorized_full[cat].append(
                (title, company, yoe, sal_min, sal_max, url, description, content_hash)
            )

    # Pagination + bounds
    categorized = {}
    total_pages = {}

    for cat in categories:
        total_jobs = len(categorized_full[cat])
        total_pages[cat] = max(1, math.ceil(total_jobs / PAGE_SIZE))

        # Clamp page to valid range
        pages[cat] = min(pages[cat], total_pages[cat])

        start = (pages[cat] - 1) * PAGE_SIZE
        end = start + PAGE_SIZE
        categorized[cat] = categorized_full[cat][start:end]

    with open(HTML_FILE, "r") as f:
        html_template = f.read()

    return render_template_string(
        html_template,
        categorized=categorized,
        pages=pages,
        total_pages=total_pages
    )

#get user feedback for updating database and model
@app.route("/update_jobs", methods=["POST"])
def update_jobs():
    delete_items = request.form.getlist("delete_items")
    irrelevant_items = request.form.getlist("irrelevant_items")
    relevant_items = request.form.getlist("relevant_items")

    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()

        for content_hash in delete_items:
            cur.execute("SELECT * FROM jobs WHERE content_hash = ?", (content_hash,))
            job = cur.fetchone()
            if job:
                cur.execute("DELETE FROM jobs WHERE content_hash = ?", (content_hash,))
                add_deleted_hash(content_hash)

        for content_hash in irrelevant_items:
            cur.execute("""
                SELECT title, description, company, yoe, salary_min, salary_max, url, category, content_hash
                FROM jobs WHERE content_hash = ?
            """, (content_hash,))
            row = cur.fetchone()
            if row:
                add_irrelevant_job({
                    "title": row[0],
                    "description": row[1],
                    "company": row[2],
                    "yoe": row[3],
                    "salary_min": row[4],
                    "salary_max": row[5],
                    "url": row[6],
                    "category": row[7],
                    "content_hash": row[8]
                })

        for content_hash in relevant_items:
            cur.execute("""
                SELECT title, description, company, yoe, salary_min, salary_max, url, category, content_hash
                FROM jobs WHERE content_hash = ?
            """, (content_hash,))
            row = cur.fetchone()
            if row:
                add_relevant_job({
                    "title": row[0],
                    "description": row[1],
                    "company": row[2],
                    "yoe": row[3],
                    "salary_min": row[4],
                    "salary_max": row[5],
                    "url": row[6],
                    "category": row[7],
                    "content_hash": row[8]
                })

    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)