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
                sh 'docker build -t flask-student-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '''
                docker stop flask-student-container || true
                docker rm flask-student-container || true
                docker run -d -p 5000:5000 --name flask-student-container flask-student-app
                '''
            }
        }
    }
}