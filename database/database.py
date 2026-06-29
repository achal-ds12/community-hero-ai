import sqlite3

DB_NAME = "issues.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS issues(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        location TEXT NOT NULL,
        image_path TEXT,
        category TEXT,
        severity TEXT,
        priority TEXT,
        department TEXT,
        summary TEXT,
        status TEXT DEFAULT 'Pending',
        reported_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def add_issue(title, description, location, image_path,
              category, severity, priority, department, summary):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO issues
    (title, description, location, image_path,
     category, severity, priority, department, summary)

    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
    (
        title,
        description,
        location,
        image_path,
        category,
        severity,
        priority,
        department,
        summary
    ))

    conn.commit()
    conn.close()


def get_all_issues():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM issues ORDER BY id DESC")

    issues = cursor.fetchall()

    conn.close()

    return issues


def update_status(issue_id, status):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE issues
    SET status=?
    WHERE id=?
    """, (status, issue_id))

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_table()
    print("Database Ready")