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
                bat 'docker rm flask-student-container || exit 0'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat '''
docker run -d ^
--name flask-student-container ^
-p 5000:5000 ^
-e DB_HOST=host.docker.internal ^
-e DB_USER=root ^
-e DB_PASSWORD=Root123 ^
-e DB_NAME=student_registration ^
flask-student-app
'''
            }
        }
    }
}