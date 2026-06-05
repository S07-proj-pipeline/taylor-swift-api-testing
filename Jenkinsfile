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

                // Limpa o registo de erros de execuções anteriores
                sh 'rm -f falhas.txt'

                // O catchError permite que o teste falhe, mas não aborte a pipeline
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    sh 'docker exec newman-runner npm run test:ci'
                }
             }
             post {
                 success { echo "API: TODAS AS REQUISIÇÕES PASSARAM" }
                 failure {
                     echo "API: FALHAS NAS REQUISIÇÕES"
                    
                     // Regista a falha no ficheiro
                     sh 'echo "Falha nos Testes Funcionais no Stage (API — Newman)" >> falhas.txt'
                 }
             }
         }

         stage('Carga e Performance - k6') {
            steps {
              echo "Executando teste de carga com k6"
              dir('k6') {
                // O catchError permite que o teste falhe, mas não aborte a pipeline
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    sh 'docker exec -i k6 k6 run /scripts/k6/load-test.js 2>&1'
                    sh 'docker exec -i k6 k6 run /scripts/k6/stress-test.js 2>&1'
                }
              }
            }
            post {
              success { echo "CARGA: Sucesso" }
              failure { 
                  echo "CARGA: Falha" 

                  // Se o k6 falhar, acrescenta esta linha ao ficheiro
                  sh 'echo "Falha nos Testes de Carga e Performance no Stage (Carga e Performance — k6)" >> falhas.txt'
              }
            }
        }
        
         stage('Build/Empacotamento') {
             steps {
                 catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                     sh 'mkdir -p artifacts'

                     sh 'cp -r /reports/* artifacts/ 2>/dev/null || true'

                     sh 'zip -r artifacts/projeto-s07.zip . -x "*.git*" "*node_modules*" "artifacts/*"'

                     writeFile file: 'artifacts/build-info.txt', text: "BUILD=${BUILD_NUMBER}"
                 }
             }
             post {
                 failure {
                     sh 'echo "Falha na geração dos Artefatos no stage (Build/Empacotamento)" >> falhas.txt'
                 }
         }

         stage('Notification') {
            steps {
                echo "Enviando e-mail de notificação dos relatórios..."
                
                withEnv(["PIPELINE_STATUS=${currentBuild.currentResult}"]) {
                    sh 'python3 send_email.py'
                }
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
            echo "Duração  : ${currentBuild.durationString}"
        }
    }
}
