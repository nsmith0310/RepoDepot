#imports
import sqlite3
import os

#database path
DB_NAME = os.path.join(os.path.dirname(__file__), "..", "db", "jobs.db")

#connect to database
def get_connection():
    return sqlite3.connect(DB_NAME)

#initialize database
def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content_hash TEXT UNIQUE,
        adzuna_id TEXT UNIQUE,
        title TEXT,
        company TEXT,
        description TEXT,
        url TEXT,
        salary_min INTEGER,
        salary_max INTEGER,
        yoe INTEGER,
        created_at INTEGER,
        category TEXT
    )
    """)

    conn.commit()
    conn.close()