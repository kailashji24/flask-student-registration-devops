# Flask Student Registration DevOps Project

## Project Overview

This project is a Flask-based Student Registration CRUD application integrated with DevOps tools and practices such as Docker, Jenkins, GitHub, and CI/CD pipeline automation.

The application allows users to:
- Add student records
- View student records
- Edit student information
- Delete student records

The project demonstrates containerization and automation using Docker and Jenkins.

---

# Features

- Create Student Records
- Read Student Data
- Update Student Information
- Delete Student Records
- Dockerized Flask Application
- Jenkins CI/CD Pipeline
- GitHub Integration
- Automated Docker Build & Deployment

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend Programming |
| Flask | Web Framework |
| SQLite | Database |
| HTML/CSS | Frontend |
| Docker | Containerization |
| Jenkins | CI/CD Automation |
| Git & GitHub | Version Control |

---

# Project Structure

```bash
flask-student-registration-devops/
│
├── models/
├── screenshots/
├── static/
├── templates/
│
├── app.py
├── config.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
├── README.md
└── .gitignore
```

---

# Application Workflow

1. User accesses Flask web application
2. User performs CRUD operations
3. Data is stored in SQLite database
4. Docker container runs the application
5. Jenkins automatically pulls code from GitHub
6. Jenkins builds Docker image
7. Jenkins deploys the container

---

# How to Run Project Locally

## Clone Repository

```bash
git clone https://github.com/kailashji24/flask-student-registration-devops.git
cd flask-student-registration-devops
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Flask Application

```bash
python app.py
```

Application runs on:

```bash
http://127.0.0.1:5000
```

---

# Docker Setup

## Build Docker Image

```bash
docker build -t flask-student-app .
```

---

## Run Docker Container

```bash
docker run -d -p 5000:5000 --name flask-student-container flask-student-app
```

---

## Stop Docker Container

```bash
docker stop flask-student-container
```

---

## Remove Docker Container

```bash
docker rm flask-student-container
```

---

# Jenkins Pipeline

This project uses Jenkins for CI/CD automation.

## Jenkins Pipeline Stages

- Clone Repository
- Build Docker Image
- Stop Old Container
- Remove Old Container
- Run New Docker Container

---

# Jenkinsfile

```groovy
pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                url: 'https://github.com/kailashji24/flask-student-registration-devops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t flask-student-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                bat 'docker stop flask-student-container || exit 0'
            }
        }

        stage('Remove Old Container') {
            steps {
                bat 'docker rm flask-student-container || exit 0'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker run -d -p 5000:5000 --name flask-student-container flask-student-app'
            }
        }
    }
}
```

---

# CI/CD Workflow

```text
Developer Pushes Code to GitHub
            ↓
Jenkins Pulls Latest Code
            ↓
Docker Image is Built
            ↓
Old Container is Removed
            ↓
New Container is Deployed
            ↓
Application Runs Automatically
```

---

# Screenshots

## Flask Application

Add screenshots inside the `screenshots/` folder.

Example:

```markdown
![Flask App](screenshots/app-home.png)
```

---

## Jenkins Pipeline

```markdown
![Jenkins Pipeline](screenshots/jenkins-pipeline.png)
```

---

## Docker Container

```markdown
![Docker Container](screenshots/docker-container.png)
```

---

# Future Improvements

- Deploy application on AWS EC2
- Use PostgreSQL/MySQL instead of SQLite
- Add Authentication System
- Implement Kubernetes Deployment
- Add GitHub Actions
- Add Monitoring using Prometheus & Grafana

---

# Learning Outcomes

Through this project, I learned:

- Flask CRUD application development
- Docker containerization
- Jenkins pipeline automation
- CI/CD concepts
- GitHub integration
- DevOps workflow implementation

---

# Author

## Kailash Chaudhary

GitHub:
https://github.com/kailashji24

---

# Repository Link

https://github.com/kailashji24/flask-student-registration-devops

---

# License

This project is created for learning and educational purposes.