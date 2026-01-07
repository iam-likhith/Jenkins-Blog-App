pipeline {
    agent any // This line specifies that the pipeline can run on any available agent
    environment {
        IMAGE = "docker.io/likhith9/flask-app"
        TAG = "${BUILD_NUMBER}"
    }
    stages {  // This block contains all the stages of the pipeline
        stage ('Build') {  // This stage is responsible for building the project
            steps {
                sh 'docker build -t "$IMAGE:$TAG" -t "$IMAGE:latest" .'
            }
        }
        stage ('Push') {  // This stage handles pushing the Images or artifacts  
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker_pat', passwordVariable: 'DOCKERHUB_PWD', usernameVariable: 'DOCKERHUB_USER')]) {
                    sh '''
                    echo "$DOCKERHUB_PWD" | docker login -u "$DOCKERHUB_USER" --password-stdin
                    docker push "$IMAGE:$TAG"
                    docker push "$IMAGE:latest"
                    '''
}
            }
        }
        stage ('Deploy') {  // This stage is for deploying the application
            steps {
                sh ''' 
                docker pull "$IMAGE:$TAG"
                docker rm -f flask-app || true 
                docker run -d --name flask-app -p 5000:5000 "$IMAGE:$TAG"

                cat <<EOF > artifact_$BUILD_NUMBER.txt 
                Application Deployed Successfully to Docker Hub.
                Build Number: $BUILD_NUMBER
                Image: $IMAGE:$TAG
                Branch: $GIT_BRANCH
                Commit: ${GIT_COMMIT}
                Time: $(date +"%Y-%m-%d_%H-%M-%S")
                URL: $BUILD_URL
                EOF
                '''
                archiveArtifacts artifacts: "artifact_${env.BUILD_NUMBER}.txt", fingerprint: true
            }
        }
        stage ('Test') {  // This stage is for running smoke tests on the deployed application
            steps {
                sh 'sleep 2; echo "Hit http://localhost:5000 to see the app."'
            }
        }
        stage ('Cleanup') {  // This stage is for cleaning up resources after deployment
            steps {
                cleanWs()
            }
        }

    }
    //post actions to be performed after the stages
    post {
        success {
            echo ' Build ${env.BUILD_NUMBER} Pipeline completed successfully!'
        }
        failure {
            echo 'Build ${env.BUILD_NUMBER} Pipeline failed. Please check the logs for details.'
        }
        always {
            echo 'Build ${env.BUILD_NUMBER} This will always run after the stages are complete.'
        }
    }
}
