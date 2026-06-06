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
A coleção de testes foi criada no Postman, utilizando scripts post-request para validar as respostas da API diretamente após cada requisição.

### Newman
Ferramenta CLI para execução da coleção Postman via terminal. Os relatórios HTML foram gerados pelo newman-reporter-htmlextra e armazenados como artefatos no Jenkins.

### K6
Ferramenta de testes de performance utilizada para simular cenários de carga e stress na API. Os scripts em JavaScript geram relatórios HTML salvos em volume compartilhado com o Nginx.

### Jenkins
Servidor de CI/CD utilizado para automatizar a pipeline. Configurado inteiramente como código via Dockerfile, Jenkinsfile e casc.yaml — sem uso de interface gráfica para criação de etapas.

### Docker e Docker Compose
Toda a infraestrutura é definida como código. O Docker Compose orquestra 6 containers: Jenkins, Newman, k6, Nginx, MailHog e smtp-relay, todos integrados via rede bridge dedicada.

### MailHog
Servidor SMTP de desenvolvimento utilizado para interceptar e visualizar os e-mails enviados ao final da pipeline, sem necessidade de configuração de servidor real.

### Nginx
Servidor web utilizado para servir os relatórios de teste gerados pela pipeline, acessíveis via browser após a execução.

### ngrok
Ferramenta de tunelamento utilizada para expor o Jenkins localmente para a internet, permitindo o funcionamento do webhook do GitHub.

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
* Notification - envia e-mail ao final da pipeline

![jenkins-pipeline](https://i.imgur.com/vuK2Phj.png)

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

Durante o projeto, todos os colaboradores utilizaram ferramentas de IA como apoio. 
O uso foi declarado individualmente por cada integrante e documentado abaixo.
Os modelos utilizados foram **Claude Sonnet 4.6** (Anthropic), **Gemini** (Google) e **DeepSeek** (modo thinking).

### Dinâmica geral
O uso foi predominantemente individual, durante o desenvolvimento de cada componente. 
Em alguns momentos foi utilizado como pair programming para depuração de erros, 
especialmente relacionados a caminhos de arquivo no contexto Docker e diferenças entre sistemas operacionais.

Um problema recorrente identificado foi a conversão de line endings de LF para CRLF pelo 
JetBrains WebStorm no Windows, que quebrava o `docker-entrypoint.sh`. 
A IA auxiliou na identificação da causa e na correção via `.gitattributes`.

### Jenkins 
Os arquivos `Jenkinsfile` e `Dockerfile` do Jenkins foram inicialmente baseados nos 
exemplos de sala de aula e posteriormente adaptados com auxílio do DeepSeek (modo thinking). 
O `casc.yaml` partiu de um template gerado pelo Gemini e foi incrementado com o Claude, 
principalmente durante a configuração do webhook com GitHub e ngrok.

**Exemplo de prompt utilizado:**
> *"Preciso configurar um webhook do GitHub para disparar o Jenkins em container Docker. 
> O ngrok já expõe a porta 8080. Como adaptar esse tutorial para funcionar via casc.yaml 
> sem usar a interface gráfica do Jenkins?"*

A resposta foi aceita parcialmente — a estrutura do `casc.yaml` foi utilizada, 
mas foi necessário iterar várias vezes para corrigir problemas como `location` 
dentro do bloco errado (`jenkins:` ao invés de `unclassified:`), 
Content-Type null no payload do webhook e o trigger não sendo aplicado por cache do volume.

### Newman
O Claude foi utilizado principalmente para análise do projeto como um todo e correção de erros de caminho no contexto Docker. 

### E-mail 
O Gemini foi utilizado para análise de erros no script de notificação e para 
geração da maior parte do `send_email.py`.

O script gerado foi aceito com pequenos ajustes de sintaxe. 
A IA também foi utilizada para dúvidas pontuais de sintaxe Python e resolução de erros.

### Testes de performance 
O Claude foi utilizado para ajustar o Dockerfile do k6/Grafana e corrigir os caminhos 
de armazenamento dos relatórios gerados.


*O Claude Sonnet 4.6 também auxiliou na revisão e formatação final do README, 
organizando as contribuições individuais de uso de IA e padronizando a estrutura do documento.*

---

### O que não foi feito por IA
- A coleção de testes do Postman foi construída manualmente, requisição por requisição
- A estrutura de organização do Docker Compose (escolha dos containers e comunicação entre eles) foi definida pelo grupo
- As decisões de arquitetura (volume compartilhado, rede bridge dedicada, separação de responsabilidades por container) foram tomadas pelo grupo
- O mapeamento dos problemas reais de execução e a validação das soluções propostas pela IA foram feitos manualmente
