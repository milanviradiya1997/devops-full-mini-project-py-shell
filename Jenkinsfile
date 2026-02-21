pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                 git branch: 'main',
            url: 'https://github.com/milanviradiya1997/devops-full-mini-project-py-shell.git'
            }
        }

        stage('Docker Deploy') {
            steps {
                sh 'bash scripts/docker_deploy.sh'
            }
        }

        stage('Log Analysis') {
            steps {
                sh 'python3 scripts/log_analysis.py'
            }
        }

        stage('Backup Logs to S3') {
            steps {
                sh 'python3 scripts/aws_s3_backup.py'
            }
        }
    }
}
