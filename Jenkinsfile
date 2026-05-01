pipeline{
    agent any
    stages{
        stage('build'){
            steps{
                echo "Building"
                sh 'docker build -t python-first-test:latest .'
            }
        }
        stage('run'){
            steps{
                echo "Running"
                sh 'docker run --rm python-first-test:latest'
            }
        }
        stage('run with env'){
            steps{
                echo "Running with environment variable"
                sh 'docker rm -f my-test-app || true'
                sh 'docker run --name my-test-app -e MY_ENV_VAR=Failt python-first-test:latest'
            }
        }
        stage('logs'){
            steps{
                echo "Logging"
                sh 'docker logs my-test-app'
            }
        }
    }
    
}
