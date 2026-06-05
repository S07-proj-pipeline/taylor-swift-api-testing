# NP2 - Aplicando DevOps na prática
## Testes de API - Taylor Swift API

Repositório dedicado à disciplina S07 - Qualidade de Software para o projeto da NP2.

Integrantes:
-
Ana Luísa Galvão Valeta | 208 <br> 
Júlio César Taranto Azevedo | 454 <br> 
Lídia Carolina de Andrade Rosa | 641 <br> 
Maria Eduarda Constância Rocha Moreira | 710

O projeto utiliza a [Taylor Swift API](https://github.com/sarbor/taylor_swift_api) criada pelo usuário [*Sarbor*](https://github.com/sarbor) no Github, sendo uma API REST pública e gratuita.

## Tecnologias

### Postman
A coleção de teste foi criada no Postman, utilizando os scripts post-request (executados após as requisições).

### Newman
Para executar os testes no terminal, foi utilizada a ferramenta Newman. O relatório HTML foi gerado pelo newman-reporter-htmlextra.

### K6
Para realizar os testes de performance, foi utilizado o k6, com scripts js para executar.

### Jenkins
Para implementar a pipeline, foi utilizado o Jenkins.

### Mailhog
O mailhog foi utilizado para realizar o envio de e-mails.

*As ferramentas foram escolhidas conforme exemplos dados em sala de aula.*

## Pré-requisitos
* Docker 

## Instalação

```bash
git clone "https://github.com/S07-proj-pipeline/taylor-swift-api-testing/"

cd taylor-swift-api-testing

``` 

É necessário configurar as variáveis de ambiente. Para isso, copie o arquivo .env.example e substitua os valores.

```bash
cp .env.example .env
```

## Para iniciar o docker

Na raiz do projeto:

```bash
    docker compose up --build
```

Para utilizar o webhook, é necessário criar um token clássico no Github, com a configuração "repo" selecionada. O token deve ser substituído também no .env. No cenário real, a build será realizada a cada push no repositório.
A configuração do Jenkins é feita pelo arquivo casc.yaml. O jenkins também está exposto via ngrok para o funcionamento adequado do webhook (desabilitado momentaneamente por razões de segurança).

A pipeline tem 4 jobs:
* Testes \
├── Teste da API com Newman \
├── Teste de performance com k6
* Build/empacotamento (cria um arquivo .zip do projeto e dos relatórios gerados)
* Notificação - envia e-mail ao final da pipeline

## Estrutura do Projeto
```bash
.
├── Jenkinsfile
├── README.md
├── collections
│   └── taylor-swift-api-testing.postman_collection.json
├── docker-compose.yml
├── docs
│   └── swagger.yaml
├── jenkins
│   ├── Dockerfile
│   ├── casc.yaml
│   ├── docker-entrypoint.sh
│   └── plugins.txt
├── k6
│   ├── Dockerfile
│   ├── load-test.js
│   ├── reports
│   │   ├── load-summary.html
│   │   └── stress-summary.html
│   └── stress-test.js
├── newman
│   ├── Dockerfile
│   └── reports
│       └── relatorio.html
├── nginx
│   ├── Dockerfile
│   └── index.html
├── package-lock.json
├── package.json
└── send_email.py

```

## Organização do projeto em grupo

Para versionamento, foi utilizado git com uma branch develop. Inicialmente, cada integrante ficou responsável por uma tarefa maior relacionada à Devops, conforme imagem abaixo do Trello. Porém, ao decorrer do projeto, todos auxiliaram em diferentes etapas.

![trello-organizatio-proj-s07](https://i.imgur.com/sCeXDvl.png)


## Uso de IA
Durante a realização do projeto, todos os colaboradores contaram com o auxílio de IA. Notou-se que o principal uso foi para identificação e correção de erros de caminho, devido ao context do Docker. Também houveram problemas como encriptação, provavelmente causado pela diferença de sistemas operacionais utilizados pelos membros (MacOS, Linux e Windows). O Jetbrains WebStorm no Windows convertia o arquivo de LF para CLRF, que quebrava o arquivo docker-entrypoint.

### IA no Jenkins
Os arquivos Jenkinsfile e Dockerfile.jenkins inicialmente foram copiados dos exemplos de sala. 