pipeline {
    agent {
        docker {
            image 'alpine:latest'
            args '-u root'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Tests') {
            steps {
                echo "running tests"
            }
        }

        stage('Build') {
            steps {
                echo "build step"
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished'
        }
    }
}
