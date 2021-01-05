def region = 'ap-southeast-1'
def bucket = 'alz-lambda-bucket'
def bundleName = 'bundle'
def s3Folder = 'lambda'
def functionName = 'parserData'
def description = 'Deploy driver es transformer'
def lambdaRole = 'arn:aws:iam::758354202054:role/lambda_deploy_role'

pipeline {
  agent any

  stages {
      stage('Checkout') {
        steps {
          git 'https://github.com/Neungzad/sample-deploy-lampda.git'
        }
      }

      stage('Zip File') {
        steps {
          sh 'pip3 install --target=./ -r requirements.txt'
          sh "zip -r ${bundleName}.zip ."
        }
      }

      stage('Upload to S3') {
        steps {
          withAWS(region: "${region}") {
            s3Upload(
              bucket:"${bucket}",
              file: "${bundleName}.zip",
              path: "${s3Folder}/",
              workingDir:'./'
            )
          }
        }
      }

      stage('Deploy lambda code') {
        steps {
          deployLambda([
            alias: '',
            artifactLocation: "s3://${bucket}/${s3Folder}/${bundleName}.zip",
            awsAccessKeyId: '$AWS_ACCESS_KEY_ID',
            awsRegion: '$AWS_DEFAULT_REGION',
            awsSecretKey: '{AQAAABAAAAAgs2ZxJxdTUWZbMmk1k8M/d1Ki9nCKgqMgywJGZALWoLRxZRZ/W41de329qoPQ2bFM}',
            deadLetterQueueArn: '',
            description: "${description}",
            environmentConfiguration: [kmsArn: ''],
            functionName: "${functionName}",
            handler: 'lambda_function.lambda_handler',
            memorySize: '1024',
            role: "${lambdaRole}",
            runtime: 'python3.8',
            securityGroups: '',
            subnets: '',
            timeout: '60',
            updateMode: 'full'])
        }
      }
  }
}

