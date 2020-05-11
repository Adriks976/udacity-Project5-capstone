pipeline {
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
        sh 'echo "$DOCKER_TOKEN" | docker login -u adrik976 --password-stdin'
        sh 'docker build --tag adrik976/udacity-capstone:latest .'
      }
    }
    
  }
}