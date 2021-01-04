def bucket = 'alz-lambda-bucket'
def bundleName = 'bundle'

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
          sh "zip -r ${bundleName}.zip ."
        }
      }

      stage('Upload to S3') {
        steps {
          withAWS(region: 'ap-southeast-1') {
            s3Upload(
              bucket:"${bucket}",
              file: "${bundleName}.zip",
              path:'lambda/',
              workingDir:'./'
            )
          }
        }
      }

      stage('Deploy lambda code') {
        steps {
          deployLambda([
            alias: '',
            artifactLocation: 's3://alz-lambda-bucket/lambda/bundle.zip',
            awsAccessKeyId: '$AWS_ACCESS_KEY_ID',
            awsRegion: '$AWS_DEFAULT_REGION',
            awsSecretKey: '{AQAAABAAAAAgs2ZxJxdTUWZbMmk1k8M/d1Ki9nCKgqMgywJGZALWoLRxZRZ/W41de329qoPQ2bFM}',
            deadLetterQueueArn: '',
            description: 'Deploy driver es transformer',
            environmentConfiguration: [kmsArn: ''],
            functionName: 'parserData',
            handler: 'lambda_function.lambda_handler',
            memorySize: '1024',
            role: 'arn:aws:iam::758354202054:role/lambda_deploy_role',
            runtime: 'python3.8',
            securityGroups: '',
            subnets: '',
            timeout: '60',
            updateMode: 'full'])
        }
      }
  }
}

