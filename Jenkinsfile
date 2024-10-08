pipeline {
    agent any
    environment{
        registry='nitingoyal/order-service'
        region='us-east-1'
    }
    options {
        timestamps()
    }
    stages {
        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build . -t order-service
                '''
            }
        }
        stage ('Docker run test') {
            steps {
                sh "docker run -p 5000:5000 -d --name order-service${BUILD_NUMBER} order-service"
                sh "sleep 5s"
            }
        }
        stage ('Clean running docker') {
            steps {
                sh "docker stop order-service${BUILD_NUMBER}"
                sh "docker rm order-service${BUILD_NUMBER}"
            }
        }
        stage('Push Image to DockerHub') {
            steps {
                sh 'docker tag order-service ${registry}:${BUILD_NUMBER}'
                sh 'docker tag order-service ${registry}:latest'
                withDockerRegistry([credentialsId: 'DockerHub', url: '']){
                    sh 'docker push ${registry}:${BUILD_NUMBER}'
                    sh 'docker push ${registry}:latest'
                }
            }
        }
        stage('Docker Deployment') {
            steps {
                withCredentials([aws(credentialsId: "nagarro")]) {
                    sh ''' 
                    aws cloudformation deploy \
                    --stack-name OrderServiceStack \
                    --template-file ./deployment.yaml \
                    --parameter-overrides ImageRepository=${registry}:${BUILD_NUMBER} \
                    --capabilities CAPABILITY_NAMED_IAM  \
                    --no-fail-on-empty-changeset \
                    --region us-east-1
                    '''
                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}