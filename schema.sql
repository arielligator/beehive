-- Drop tables if they already exist (for development only)
DROP TABLE IF EXISTS person_works_with;
DROP TABLE IF EXISTS person_jobs;
DROP TABLE IF EXISTS person_departments;
DROP TABLE IF EXISTS works_with;
DROP TABLE IF EXISTS jobs;
DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS people;

-- Core tables
CREATE TABLE people (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    dob TEXT,
    phone TEXT,
    email   TEXT,
    address TEXT
);

CREATE TABLE departments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE works_with (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);


-- Join tables
CREATE TABLE person_departments (
    person_id   INTEGER NOT NULL,
    department_id INTEGER NOT NULL,
    PRIMARY KEY (person_id, department_id),
    FOREIGN KEY (person_id) REFERENCES people(id),
    FOREIGN KEY (department_id) REFERENCES departments(id)
);

CREATE TABLE person_jobs (
    person_id INTEGER NOT NULL,
    job_id INTEGER NOT NULL,
    PRIMARY KEY (person_id, job_id),
    FOREIGN KEY (person_id) REFERENCES people(id),
    FOREIGN KEY (job_id) REFERENCES jobs(id)
);

CREATE TABLE person_works_with (
    person_id INTEGER NOT NULL,
    works_with_id INTEGER NOT NULL,
    PRIMARY KEY (person_id, works_with_id),
    FOREIGN KEY (person_id) REFERENCES people(id),
    FOREIGN KEY (works_with_id) REFERENCES works_with(id)
);