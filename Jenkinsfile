pipeline {
    agent any

    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Checkout') {
            steps {
                // Checkout your source code from version control
                checkout scm
            }
        }

        stage('Run Python scripts') {
            steps {
                script {
                    sh "python3 tools/generate_hosts_file.py"
                }
                script {
                    sh "python3 tools/generate_ssh_config.py"
                }
            }
        }

        stage('Run Ansible Playbook') {
            steps {
                ansiblePlaybook(
                    playbook: 'main.yml',
                    inventory: 'inventory.ini')
            }
        }
    }
}

