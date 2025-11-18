
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
                bat "C:\\Users\\S\\AppData\\Local\\Programs\\Python\\Python313\\python.exe extract.py"
            }
        }
    }
}