def bucket = 'alz-lambda-bucket'
// def functionName = 'lambdaJa'
// def region = 'eu-west-3'

pipeline {
  agent any

  stages {
      stage('Checkout') {
        steps {
          git 'https://github.com/Neungzad/sample-deploy-lampda.git'
        }
      }

      // stage('Run Unit Test') {
      //   steps {
      //     echo 'run test'
      //   }
      // }

      stage('Zip File') {
        steps {
          sh "zip -r ${commitID()}.zip ."
        }
      }

      stage('Upload to S3') {
        steps {
          withAWS(region: 'ap-southeast-1') {
            s3Upload(
              bucket:"${bucket}",
              file: "${commitID()}.zip",
              path:"lambda/",
              // includePathPattern:'',
              workingDir:'./'
            )
          }
        }
      }
  }
}

def commitID() {
  // sh 'git rev-parse HEAD > .git/commitID'
  // def commitID = readFile('.git/commitID').trim()
  // sh 'rm .git/commitID'
  'bundle'
}
