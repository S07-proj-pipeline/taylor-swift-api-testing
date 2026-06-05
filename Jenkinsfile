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
                        echo "Executando testes da API com Newman"
                        sh 'docker exec newman-runner npm run test:ci'
                    }
                     post {
                         success { echo "API: TODAS AS REQUISIÇÕES PASSARAM" }
                         failure { echo "API: FALHAS NAS REQUISIÇÕES" }
                     }
                 }

                 stage('Carga e Performance — k6') {
                    steps {
                      echo "Executando teste de carga com k6"
                      dir('k6') {
                        sh 'docker exec k6 k6 run /scripts/k6/load-test.js'
                        sh 'docker exec k6 k6 run /scripts/k6/stress-test.js'
                      }
                    }
                    post {
                      success { echo "CARGA: Sucesso" }
                      failure { echo "CARGA: Falha" }
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
