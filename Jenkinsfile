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
  }
}
