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