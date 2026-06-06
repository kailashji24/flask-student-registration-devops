# Student Registration DevOps Platform

A production-style Student Registration Management System built using Flask, MySQL, SQLAlchemy, Docker, Docker Compose, and Jenkins.

This project demonstrates CRUD operations, containerized deployment, database integration, CI/CD automation, environment-based configuration, and multi-container application management.

---

## Project Architecture

```text
User
  |
Flask Application (Gunicorn)
  |
MySQL Database
```

Containerized Architecture:

```text
Docker Compose
│
├── Flask Container
│   ├── Flask
│   ├── SQLAlchemy
│   └── Gunicorn
│
└── MySQL Container
    └── Persistent Volume
```

---

## Features

* Student Registration CRUD Operations
* Create Student Records
* View Registered Students
* Update Student Information
* Delete Student Records
* Input Validation
* MySQL Database Integration
* SQLAlchemy ORM
* Docker Containerization
* Multi-Container Deployment using Docker Compose
* Jenkins CI/CD Pipeline
* Environment Variable Configuration
* Persistent Database Storage
* MySQL Health Checks
* Gunicorn Production Server

---

## Technology Stack

### Backend

* Flask
* SQLAlchemy
* Gunicorn

### Database

* MySQL 8

### DevOps

* Docker
* Docker Compose
* Jenkins

### Version Control

* Git
* GitHub

### Frontend

* HTML
* CSS
* Bootstrap

---

## Project Structure

```text
project_3_flaskapp/
│
├── app.py
├── config.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
├── .env.example
├── README.md
│
├── models/
│   └── student.py
│
├── templates/
│   ├── index.html
│   └── students.html
│
├── static/
│
└── screenshots/
```

---

## Environment Variables

Create a .env file using the provided .env.example file.

Example:

```env
SECRET_KEY=replace-with-secret-key

DB_USER=replace-with-db-user
DB_PASSWORD=replace-with-db-password
DB_NAME=student_registration
DB_HOST=mysql
DB_PORT=3306

MYSQL_ROOT_PASSWORD=replace-with-root-password
MYSQL_DATABASE=student_registration
MYSQL_USER=replace-with-db-user
MYSQL_PASSWORD=replace-with-db-password
```

---

## Running the Application

### Clone Repository

```bash
git clone https://github.com/kailashji24/flask-student-registration-devops.git
cd flask-student-registration-devops
```

### Create Environment File

```bash
cp .env.example .env
```

### Start Application

```bash
docker compose up -d --build
```

### Check Containers

```bash
docker compose ps
```

### View Logs

```bash
docker compose logs -f
```

### Access Application

```text
http://localhost:5000
```

---

## Stopping the Application

Stop containers:

```bash
docker compose down
```

Stop containers and remove database volume:

```bash
docker compose down -v
```

---

## Jenkins Pipeline

The Jenkins pipeline automates:

1. Source Code Checkout
2. Docker Compose Validation
3. Docker Image Build
4. Container Deployment
5. Service Verification

Pipeline Stages:

```text
Clone Repository
      ↓
Validate Compose File
      ↓
Build Containers
      ↓
Deploy Application
      ↓
Verify Services
```

---

## Docker Compose Services

### Flask Service

* Flask Application
* Gunicorn Web Server
* SQLAlchemy ORM
* Environment-Based Configuration

### MySQL Service

* MySQL 8 Database
* Persistent Storage
* Health Checks
* Automatic Service Recovery

---

## Key DevOps Concepts Demonstrated

* Containerization
* Multi-Container Architecture
* Infrastructure Automation
* CI/CD Pipelines
* Environment Management
* Service Networking
* Database Persistence
* Health Monitoring
* Production Web Server Deployment

---

## Screenshots

Add project screenshots inside:

```text
screenshots/
```

Example:

* Application Home Page
* Student Registration Form
* Student List Page
* Docker Containers Running
* Jenkins Successful Pipeline
* Docker Compose Services

---

## Resume Project Description

Student Registration DevOps Platform

Flask · MySQL · SQLAlchemy · Docker · Docker Compose · Jenkins · Gunicorn

Developed a Student Registration CRUD application using Flask, SQLAlchemy, and MySQL. Containerized the application with Docker and implemented a multi-container architecture using Docker Compose. Configured persistent database storage, environment-based configuration management, health checks, and service networking. Built a Jenkins CI/CD pipeline to automate application build, validation, and deployment workflows. Deployed the application using Gunicorn as a production-grade WSGI server and managed service orchestration through Docker Compose.

---

## Author

Kailash Chaudhary

GitHub:
https://github.com/kailashji24

Project Repository:
https://github.com/kailashji24/flask-student-registration-devops
