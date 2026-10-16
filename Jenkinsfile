pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                checkout scm
                echo 'Repository checkout completed'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m venv .venv'
                bat '.venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat '.venv\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '.venv\\Scripts\\python.exe -m pytest -v'
            }
        }

        stage('Build') {
            steps {
                bat '.venv\\Scripts\\python.exe app.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deployment Successful (simulation only)'
            }
        }
    }

    post {
        success {
            echo 'CI/CD pipeline completed successfully.'
        }

        failure {
            echo 'Pipeline failed. Check the Console Output.'
        }
    }
}
