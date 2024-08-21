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