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

    conn.execute("""
    CREATE TABLE IF NOT EXISTS project_artifacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        initiative_id INTEGER,
        artifact_type TEXT,
        content TEXT,
        status TEXT,
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

def save_artifact(
    initiative_id,
    artifact_type,
    content,
    status="approved"
):

    conn = sqlite3.connect(DB_PATH)

    conn.execute("""
    INSERT INTO project_artifacts (
        initiative_id,
        artifact_type,
        content,
        status
    )
    VALUES (?, ?, ?, ?)
    """, (
        initiative_id,
        artifact_type,
        content,
        status
    ))

    conn.commit()
    conn.close()
def get_artifact(
    initiative_id,
    artifact_type
):

    conn = sqlite3.connect(DB_PATH)

    row = conn.execute("""
    SELECT content
    FROM project_artifacts
    WHERE initiative_id = ?
    AND artifact_type = ?
    ORDER BY id DESC
    LIMIT 1
    """, (
        initiative_id,
        artifact_type
    )).fetchone()

    conn.close()

    return row
