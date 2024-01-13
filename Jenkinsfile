pipeline {
    agent any

    parameters {
        string(name: 'INSTANCE',
            description: 'Specify the instance variable')
        string(name: 'TAGS',
            description: 'Options: base, docker, production')
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout your source code from version control
                checkout scm
            }
        }

        stage('Run Ansible Playbook') {
            steps {
                ansiblePlaybook(
                    playbook: 'main.yml',
                    inventory: 'inventory.ini',
                    tags: params.TAGS,
                    extraVars: [
                        instance: params.INSTANCE
                    ])
            }
        }
    }
}

