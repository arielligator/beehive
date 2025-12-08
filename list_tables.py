import sqlite3

conn = sqlite3.connect("dummy_database.db")
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables:", tables)

print("\nPeople:")
cursor.execute("SELECT * FROM people LIMIT 5;")
for row in cursor.fetchall():
    print(row)

print("\nDepartments:")
cursor.execute("SELECT * FROM departments;")
for row in cursor.fetchall():
    print(row)

print("\nPerson ↔ Departments:")
cursor.execute("SELECT * FROM person_departments LIMIT 10;")
for row in cursor.fetchall():
    print(row)

print("\nJobs:")
cursor.execute("SELECT * FROM jobs;")
for row in cursor.fetchall():
    print(row)

print("\nPerson ↔ Jobs:")
cursor.execute("SELECT * FROM person_jobs LIMIT 10;")
for row in cursor.fetchall():
    print(row)

conn.close()
