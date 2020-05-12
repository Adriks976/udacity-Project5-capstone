pipeline {
  environment {
    dockerhubCredentials = 'dockerhubCredentials'
  }
  agent any
  stages {
    stage('Install dependencies') {
      steps {
        sh 'python3 -m venv venv'
        sh '. venv/bin/activate && make install'
      }
    }
    stage('Lint') {
      steps {
        sh '. venv/bin/activate && make lint'
      }
    }
    stage('Build docker') {
      steps {
        script {
          app = docker.build("adrik976/udacity-capstone")
        }
      }
    }
    
    stage('Scan image') {
      steps {
                aquaMicroscanner imageName: "adrik976/udacity-capstone", notCompliesCmd: 'exit 4', onDisallowed: 'ignore', outputFormat: 'html'
            }
        }
    stage('Publish docker') {
      steps {
        script {
          docker.withRegistry('', dockerhubCredentials) {
            app.push()
          }
        }
      }
    }
    
  }
}