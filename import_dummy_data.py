import sqlite3
from pathlib import Path

import pandas as pd

DB_PATH = Path("dummy_database.db")
EXCEL_PATH = Path("dummy_database.xlsx")

def main():
    # connect to the database
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # load excel file into dataframe
    df = pd.read_excel(EXCEL_PATH)

    # loop through each row and insert into tables
    for _, row in df.iterrows():
        first_name = str(row["NAME"]).strip()
        last_name = str(row["SURNAME"]).strip()
        email = str(row.get("EMAIL", "")).strip()
        phone  = str(row.get("PHONE", "")).strip()
        address = str(row.get("ADDRESS", "")).strip()

        # insert into people table
        cursor.execute(
            """
            INSERT INTO people (first_name, last_name, email, phone, address)
            VALUES (?, ?, ?, ?, ?)
            """,
            (first_name, last_name, email, phone, address),
        )
        person_id = cursor.lastrowid

        # departments from DEPARTMENT column
        dept_cell = row.get("DEPARTMENT")
        if pd.notna(dept_cell):
            dept_names = [d.strip() for d in str(dept_cell).split(",") if d.strip()]
            for dept_name in dept_names:
                # ensure department exists
                cursor.execute(
                    "INSERT OR IGNORE INTO departments (name) VALUES (?)",
                    (dept_name,),
                )
                # get its id
                cursor.execute(
                    "SELECT id FROM departments WHERE name = ?",
                    (dept_name,),
                )
                dept_id = cursor.fetchone()[0]

                # link person to department(s) in join table
                cursor.execute(
                    """
                    INSERT OR IGNORE INTO person_departments (person_id, department_id)
                    VALUES (?, ?)
                    """,
                    (person_id, dept_id),
                )

        # jobs from JOBS column
        job_cell = row.get("JOBS")
        if pd.notna(job_cell):
            job_names = [d.strip() for d in str(job_cell).split(",") if d.strip()]
            for job_name in job_names:
                # ensure department exists
                cursor.execute(
                    "INSERT OR IGNORE INTO jobs (name) VALUES (?)",
                    (job_name,),
                )
                # get its id
                cursor.execute(
                    "SELECT id FROM jobs WHERE name = ?",
                    (job_name,),
                )
                job_id = cursor.fetchone()[0]

                # link person to job(s) in join table
                cursor.execute(
                    """
                    INSERT OR IGNORE INTO person_jobs (person_id, job_id)
                    VALUES (?, ?)
                    """,
                    (person_id, job_id),
                )

        # TODO: import jobs

    conn.commit()
    conn.close()
    print("Imported data from dummy_database.xlsx into dummy_database.db")

if __name__ == "__main__":
    main()