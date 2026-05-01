pipeline{
    agent any
    stages{
        stage('build'){
            steps{
                echo "Building"
                sh 'sudo apt update'
                sh 'sudo apt install docker.io -y'
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
                sh 'docker run -e MY_ENV_VAR=Fail python-first-test:latest'
            }
        }
        stage('logs'){
        steps{
            echo "Loggins"
            sh 'docker logs python-first-test:latest'
        }
    }
    }
    
}