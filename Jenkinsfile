pipeline {
    agent any
    stages {

        stage('login') {
            steps {
                sh 'aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 027250925259.dkr.ecr.us-east-1.amazonaws.com'
            }
        }

        stage('build') {
            steps {
                sh 'docker build -t demo-app .'
            }
        }

         stage('tag') {
            steps {
                sh 'docker tag demo-app:latest 027250925259.dkr.ecr.us-east-1.amazonaws.com/demo-app:latest'
            }
        }

        stage('push') {
            steps {
                sh 'docker push 027250925259.dkr.ecr.us-east-1.amazonaws.com/demo-app:latest'
            }
        }

    }
}
