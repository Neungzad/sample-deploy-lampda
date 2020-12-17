def bucket = 'alz-lambda-bucket'
// def functionName = 'lambdaJa'
// def region = 'eu-west-3'

pipeline {
  agent any

  stages {
      stage('Hello') {
        steps {
          echo 'Hello World ja'
        }
      }

      stage('Checkout') {
        steps {
          git 'https://github.com/Neungzad/sample-deploy-lampda.git'
        }
      }

      stage('Test') {
        steps {
          echo 'run test'
        }
      }

      stage('Build') {
        steps {
          sh "zip ${commitID()}.zip ."
        }
      }

      stage('Push'){
        steps {
          sh "aws s3 cp ${commitID()}.zip s3://${bucket}"
        }
      }
  }
}

def commitID() {
    sh 'git rev-parse HEAD > .git/commitID'
    def commitID = readFile('.git/commitID').trim()
    sh 'rm .git/commitID'
    commitID
}
