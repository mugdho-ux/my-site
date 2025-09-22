pipeline {
    agent any

    environment {
        CHROME_DRIVER = 'chromedriver.exe'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/mugdho-ux/my-site.git'
            }
        }

        stage('Install Python Dependencies') {
            steps {
                sh 'pip install selenium'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'python3 tests/test_A.py'
            }
        }

        stage('Build') {
            steps {
                echo 'No build needed for static website'
            }
        }

        stage('Deploy') {
            steps {
                sh 'cp -r * /var/www/html/my-website/'  // Example: Linux server deployment
                echo 'Website deployed successfully!'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished'
        }
        success {
            echo 'All stages passed'
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}
