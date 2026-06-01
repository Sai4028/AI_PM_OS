import sqlite3
DB_PATH = "ai_pm_os.db"


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


def get_initiative_by_id(initiative_id):
    conn = sqlite3.connect(DB_PATH)

    row = conn.execute("""
    SELECT *
    FROM initiatives
    WHERE id = ?
    """, (initiative_id,)).fetchone()

    conn.close()

    return row
