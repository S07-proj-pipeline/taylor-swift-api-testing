pipeline {

    agent any

    options {
        timeout(time: 30, unit: 'MINUTES')
        buildDiscarder(logRotator(numToKeepStr: '5', artifactNumToKeepStr: '5'))
        timestamps()
        ansiColor('xterm')
        disableConcurrentBuilds()
    }

    stages {
        
         stage('API - Newman') {

            steps {
                echo "Executando testes da API com Newman"
                sh 'docker exec newman-runner npm run test:ci'
             }
             post {
                 success { echo "API: TODAS AS REQUISIÇÕES PASSARAM" }
                 failure { echo "API: FALHAS NAS REQUISIÇÕES" }
             }
         }

         stage('Carga e Performance - k6') {
            steps {
              echo "Executando teste de carga com k6"
              dir('k6') {
                sh 'docker exec -i k6 k6 run /scripts/k6/load-test.js 2>&1'
                sh 'docker exec -i k6 k6 run /scripts/k6/stress-test.js 2>&1'
              }
            }
            post {
              success { echo "CARGA: Sucesso" }
              failure { echo "CARGA: Falha" }
            }
        }
        
         stage('Build/Empacotamento') {
             steps {
                     sh 'mkdir -p artifacts'

                     sh 'cp -r /reports/* artifacts/ 2>/dev/null || true'

                     sh 'zip -r artifacts/projeto-s07.zip . -x "*.git*" "*node_modules*" "artifacts/*"'

                     writeFile file: 'artifacts/build-info.txt', text: "BUILD=${BUILD_NUMBER}"
                 }
         }

         stage('Notification') {
            steps {
                echo "Enviando e-mail de notificação dos relatórios..."
                sh 'python3 send_email.py'
            }
         }

    }

    post {
        success {
          echo "Pipeline concluído com SUCESSO!"
          archiveArtifacts artifacts: 'artifacts/projeto-s07.zip, artifacts/*.html, artifacts/*.json', fingerprint: true
        }
        failure { echo "Pipeline FALHOU. Verificar logs acima." }
        unstable { echo "Pipeline INSTÁVEL — alguns testes falharam." }
        always {
            echo "Pipeline : ${env.NOME_PIPELINE ?: 'taylor-swift-api-testing-pipeline'}"
            echo "Build    : #${BUILD_NUMBER}"
            echo "Resultado: ${currentBuild.currentResult}"
            echo "Duração  : ${currentBuild.durgtationString}"
        }
    }
}
