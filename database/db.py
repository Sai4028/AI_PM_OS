import sqlite3
from pathlib import Path

DB_PATH = "data/ai_pm_os.db"

Path("data").mkdir(exist_ok=True)

def init_db():
    conn = sqlite3.connect(DB_PATH)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS initiatives (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        industry TEXT,
        problem_statement TEXT,
        target_users TEXT,
        business_goal TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def create_initiative(
    name,
    industry,
    problem_statement,
    target_users,
    business_goal
):
    conn = sqlite3.connect(DB_PATH)

    conn.execute("""
    INSERT INTO initiatives (
        name,
        industry,
        problem_statement,
        target_users,
        business_goal
    )
    VALUES (?, ?, ?, ?, ?)
    """, (
        name,
        industry,
        problem_statement,
        target_users,
        business_goal
    ))

    conn.commit()
    conn.close()


def get_initiatives():
    conn = sqlite3.connect(DB_PATH)

    rows = conn.execute("""
    SELECT *
    FROM initiatives
    ORDER BY id DESC
    """).fetchall()

    conn.close()

    return rows
