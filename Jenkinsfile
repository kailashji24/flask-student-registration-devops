pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main',
                url: 'https://github.com/kailashji24/flask-student-registration-devops.git'
            }
        }

        stage('Validate Docker Compose') {
            steps {
                bat 'docker compose config'
            }
        }

        stage('Build Services') {
            steps {
                bat 'docker compose build --pull'
            }
        }

        stage('Deploy Services') {
            steps {
                bat 'docker compose up -d --remove-orphans'
            }
        }

        stage('Show Service Status') {
            steps {
                bat 'docker compose ps'
            }
        }
    }

    post {
        failure {
            bat 'docker compose logs --tail=100'
        }
    }
}
