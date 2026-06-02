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
        NOME_PIPELINE = 'taylor-swift-api-testing-pipeline'
    }

    stages {
         stage('Testes') {
             stages {
                 stage('API — Newman') {
                     steps {
                         echo "Instalando dependências"
                         dir('pipeline') {
                             sh 'npm ci'
                         }
                         echo "Executando testes"
                         dir('pipeline') {
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
            echo "Pipeline : ${env.NOME_PIPELINE ?: 'taylor-swift-api-testing-pipeline'}"
            echo "Build    : #${BUILD_NUMBER}"
            echo "Resultado: ${currentBuild.currentResult}"
            echo "Duração  : ${currentBuild.durationString}"
        }
    }
}
