# Student Registration App

A production-style local Flask application for registering students and storing records in a MySQL database.

## Features

- Student registration form with name, email, phone number, course, and address
- MySQL persistence through Flask SQLAlchemy ORM
- Server-side validation and duplicate email handling
- Flash messages for success and failure states
- Responsive Bootstrap 5 interface
- Registered students table view

## Project Structure

```text
student-registration-app/
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
├── static/
│   └── style.css
├── templates/
│   ├── index.html
│   └── students.html
├── models/
│   ├── __init__.py
│   └── student.py
└── screenshots/
```

## Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create the MySQL database:

```sql
CREATE DATABASE student_registration;
```

Set environment variables in PowerShell:

```powershell
$env:SECRET_KEY="replace-with-a-secure-secret"
$env:DB_USER="root"
$env:DB_PASSWORD="your_mysql_password"
$env:DB_HOST="localhost"
$env:DB_PORT="3306"
$env:DB_NAME="student_registration"
```

Alternatively, set a complete connection string:

```powershell
$env:DATABASE_URL="mysql+pymysql://root:your_mysql_password@localhost:3306/student_registration"
```

Run the app:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Pages

- `/` - Register a new student
- `/students` - View all registered students

## Notes

- Tables are created automatically on app startup with `db.create_all()`.
- Do not commit `.env` or local database credentials.
- Docker and Jenkins are intentionally not included yet.
