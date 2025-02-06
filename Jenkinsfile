pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    sh 'python -m venv .venv'
                    sh './.venv/Scripts/pip install -r requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    sh './.venv/Scripts/python -m unittest discover'
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    sh './.venv/Scripts/python app.py &'
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    sh 'curl http://localhost:5000/system/check'
                }
            }
        }
    }

    triggers {
        cron('15 3 * * *')
    }
}