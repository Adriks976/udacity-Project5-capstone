pipeline {
  agent any
  stages {
    stage('Install dependencies') {
      steps {
        sh 'python3 -m venv venv'
        sh '. venv/bin/activate'
        sh 'make install'
      }
    }
    stage('Lint') {
      steps {
        sh '. venv/bin/activate'
        sh 'make lint'
      }
    }
    
  }
}