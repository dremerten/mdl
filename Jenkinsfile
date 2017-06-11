/*
You will need to create the requisite db and db user on the machine using Jenkins

create database test_infoset;  
create user 'travis'@'localhost' identified by '';
grant all privileges on test_infoset.* to 'travis'@'localhost';

*/
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            
            steps {
                echo 'Testing..'
                /*
                sh 'pip3 install setuptools'
                sh 'pip3 install -r requirements.txt'
                sh 'export PYTHONPATH=${PYTHONPATH}:$(pwd)/infoset/test'
                sh 'python3 infoset/test/_do_all_tests.py'
                */
            }
        }
        stage('Deploy') {
            when {
                branch 'master'
            }
            steps{
                echo 'Deploying....'
                sh 'cp -r * /home/luke/mdl'
                sh 'cd /home/luke/mdl && nohup python3 server.py &'
            }
        }
    }
}