import sqlite3
from pathlib import Path

DB_PATH = Path("dummy_database.db") # SQLite database file
SCHEMA_PATH = Path("schema.sql")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    with SCHEMA_PATH.open("r", encoding="utf-8") as f:
        schema_sql = f.read()

    cursor.executescript(schema_sql)
    conn.commit()
    conn.close()
    print(f"Database initialized at {DB_PATH.resolve()}")

if __name__ == "__main__":
    init_db()