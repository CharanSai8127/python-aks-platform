pipeline {
    agent any

    environment {
        IMAGE_NAME   = "charansait372/python-aks-platform"
        IMAGE_TAG    = "v1.4"
        SCANNER_HOME = tool 'sonar-scanner'
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/CharanSai8127/python-aks-platform.git'
            }
        }

        stage('Build Application') {
            steps {
                sh '''
                  python3 -m venv venv
                  . venv/bin/activate

                  pip install --upgrade pip
                  pip install -r requirements.txt

                  if [ -f pytest.ini ] || [ -d tests ]; then
                    pip install pytest pytest-cov
                    pytest
                  fi
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv("sonar") {
                    sh '''
                      ${SCANNER_HOME}/bin/sonar-scanner \
                        -Dsonar.projectKey=python-aks-platform \
                        -Dsonar.sources=. \
                        -Dsonar.language=py
                    '''
                }
            }
        }

        stage('SonarQube Quality Gate') {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }

        stage('Dependency Check (OWASP)') {
            steps {
                dependencyCheck additionalArguments: '--scan ./',
                                odcInstallation: 'owasp'
                dependencyCheckPublisher pattern: '**/dependency-check-report.xml'
            }
        }

        stage('Trivy Filesystem Scan') {
            steps {
                sh '''
                  trivy fs \
                    --severity HIGH,CRITICAL \
                    --format json \
                    --output trivy-fs.json \
                    .
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                  docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                '''
            }
        }

        stage('Trivy Image Scan') {
            steps {
                sh '''
                  trivy image \
                    --severity HIGH,CRITICAL \
                    --format json \
                    --output trivy-image.json \
                    ${IMAGE_NAME}:${IMAGE_TAG}
                '''
            }
        }

        stage('Docker Push') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'docker-cred',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                      echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                      docker push ${IMAGE_NAME}:${IMAGE_TAG}
                    '''
                }
            }
        }
    }

    post {
        always {
            sh 'rm -rf venv'
        }

        success {
            echo " CI pipeline completed successfully"

            archiveArtifacts artifacts: '''
                **/dependency-check-report.xml,
                **/dependency-check-report.html,
                trivy-fs.json,
                trivy-image.json,
                .scannerwork/**
            ''', allowEmptyArchive: true
        }

        failure {
            echo " Pipeline failed"
        }
    }
}

