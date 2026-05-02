pipeline{
    agent {
        docker {
            image 'docker:24-cli'
            args '''
                --group-add 984 
                -v /var/run/docker.sock:/var/run/docker.sock 
                -e HOME=/home/jenkins
            '''
        }
    }

    stages {
        stage('prepare env') {
            steps {
                sh '''
                    mkdir -p /home/jenkins
                    chown -R 1000:1000 /home/jenkins
                '''
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
