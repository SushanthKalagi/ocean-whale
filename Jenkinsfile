pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    bat 'python -m venv .venv'
                    bat '.\\.venv\\Scripts\\pip install -r requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    bat '.\\.venv\\Scripts\\python -m unittest discover'
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    bat 'start /B .\\.venv\\Scripts\\python app.py'
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    bat 'curl http://localhost:5000/system/check'
                }
            }
        }
    }

    triggers {
        cron('15 3 * * *')
    }
}