pipeline {

    agent any

    options {
        timeout(time: 30, unit: 'MINUTES')
        buildDiscarder(logRotator(numToKeepStr: '5', artifactNumToKeepStr: '5'))
        timestamps()
        ansiColor('xterm')
        disableConcurrentBuilds()
    }

    environment {
        NOME_PIPELINE = 'S07 — Testes Automatizados'
    }

    stages {

        stage('Testes') {
            parallel {

                stage('Cypress — sem BDD') {
                    environment {
                        CYPRESS_defaultCommandTimeout = '10000'
                    }
                    steps {
                        echo "Instalando dependências do Cypress..."
                        dir('cypress-project') {
                            sh 'npm ci'
                        }
                        echo "Executando testes sem BDD (Page Object Model)..."
                        dir('cypress-project') {
                            sh 'npm run test:sem-bdd'
                        }
                    }
                    post {
                        success { echo "Cypress sem BDD: TODOS OS TESTES PASSARAM" }
                        failure {
                            echo "Cypress sem BDD: FALHAS DETECTADAS"
                            archiveArtifacts artifacts: 'cypress-project/cypress/screenshots/**',
                                             allowEmptyArchive: true
                        }
                    }
                }

                stage('Cypress — BDD') {
                    environment {
                        CYPRESS_defaultCommandTimeout = '10000'
                    }
                    steps {
                        echo "Instalando dependências do Cypress..."
                        dir('cypress-project') {
                            sh 'npm ci'
                        }
                        echo "Executando testes BDD (Gherkin/Cucumber)..."
                        dir('cypress-project') {
                            sh 'npm run test:bdd'
                        }
                    }
                    post {
                        success { echo "Cypress BDD: TODOS OS CENÁRIOS PASSARAM" }
                        failure {
                            echo "Cypress BDD: CENÁRIOS COM FALHA"
                            archiveArtifacts artifacts: 'cypress-project/cypress/screenshots/**',
                                             allowEmptyArchive: true
                        }
                    }
                }

                stage('API — Newman') {
                    steps {
                        echo "Instalando dependências do Newman..."
                        dir('api-testing') {
                            sh 'npm ci'
                        }
                        echo "Executando testes de API (PokéAPI)..."
                        dir('api-testing') {
                            sh 'npm test'
                        }
                    }
                    post {
                        success { echo "API: TODAS AS REQUISIÇÕES PASSARAM" }
                        failure { echo "API: FALHAS NAS REQUISIÇÕES" }
                    }
                }

            }
        }

    }

    post {
        success { echo "Pipeline concluído com SUCESSO!" }
        failure { echo "Pipeline FALHOU. Verificar logs acima." }
        unstable { echo "Pipeline INSTÁVEL — alguns testes falharam." }
        always {
            echo "Pipeline : ${env.NOME_PIPELINE ?: 'S07 — Testes Automatizados'}"
            echo "Build    : #${BUILD_NUMBER}"
            echo "Resultado: ${currentBuild.currentResult}"
            echo "Duração  : ${currentBuild.durationString}"
        }
    }

}
