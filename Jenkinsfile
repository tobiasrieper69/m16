pipeline {
    agent any
    environment { 
        registry = "tobiasreaper69/m16" 
        registryCredential = 'dockerhub' 
        dockerImage = '' 
    }

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        stage('Coffee') {
            steps {
                echo 'Hello Coffee'
            }
        }
        stage('Cal') {
            steps {
                sh 'cal'
            }
        }
        stage('Sleep') {
            steps {
                sleep time: 50, unit: 'MILLISECONDS'
            }
        }
        stage('Git Cloning'){
            steps{
                git 'https://github.com/tobiasrieper69/m16.git'
                sh 'ls -lrth'
            }
        }
        stage('Security check'){
            
            steps{
                sh 'docker run --user $(id -u):$(id -g) -v $(pwd):/src --rm nchudleigh/bandit -r /src -f json -o /src/bandit-output.json || echo '

            }
            
        }
        stage('Build docker image'){
            steps{
                script{
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                }
            }
        }
        stage('Push Image'){
            steps{
                script{
                    docker.withRegistry('', registryCredential){
                        dockerImage.push()
                    }
                    
                }
            }
        }
        stage('Clear image'){
            steps{
                sh 'docker rmi '+ registry + ':$BUILD_NUMBER'
            }
        }
        stage('Kube Apply'){
            steps{
                sh "echo Deploying to Kube"
                sh "sed -i 's/TAG/$BUILD_NUMBER/g' deployment.yaml"
                sh "kubectl apply -f deployment.yaml"
                sh "cat deployment.yaml"
            }
        }
        
    }
    post{
    	always{
    	archiveArtifacts artifacts: 'bandit-output.json', onlyIfSuccessful: true
    	}
    }
}
