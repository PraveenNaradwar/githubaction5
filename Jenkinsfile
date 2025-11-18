
pipeline{
    agent any
    stages{
        stage('checkout code'){
            steps{
                checkout scm
            }
        }
        stage('Run extarct.py'){
            steps{
                bat "python extarct.py"
            }
        }
    }
}