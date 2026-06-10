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

## Webhook (opcional)

Por padrão, o projeto roda sem webhook — a pipeline pode ser disparada manualmente ou via push no repositório com o webhook configurado.

### Configurar o webhook com ngrok
Para que um push no repositório dispare a pipeline automaticamente, é necessário 
expor o Jenkins via ngrok e configurar o webhook no GitHub.

**1. Instale e autentique o ngrok:** https://ngrok.com/download

**2. Exponha o Jenkins:**
```bash
ngrok http 8080
```

**3. Atualize o `.env` com a URL gerada pelo ngrok:**
```env
JENKINS_URL=https://seu-id.ngrok-free.app/
```

**4. Reinicie os containers:**
```bash
docker-compose down && docker-compose up --build
```

**5. Configure o webhook no GitHub:**  
Acesse **Settings > Webhooks > Add webhook** no repositório e preencha:
- Payload URL: `https://seu-id.ngrok-free.app/github-webhook/`
- Content type: `application/json`
- SSL verification: `Disable`
- Events: `Just the push event`

> ⚠️ A URL do ngrok muda a cada reinício no plano gratuito. 
> Atualize o `.env` e o webhook no GitHub sempre que isso ocorrer.


> ⚠️ No .env.example já tem a URL do ngrok exposta pela colaboradora Lídia. Porém, está desabilitada por razões de segurança e será habilitada novamente para a apresentação.

## Para iniciar o docker

Na raiz do projeto:

```bash
    docker compose up --build
```

Para visualizar os e-mails enviados pela pipeline, acesse o MailHog em `http://localhost:8025` caso o modo de envio seja configurado no `.env` como `MODO_ENVIO=local` (MailHog).  Caso seja `MODO_ENVIO=real` (SMTP externo) e os dados do Gmail forem colocados corretamente, o e-mail será enviado ao destinatário.

## Pipeline

A pipeline tem 4 jobs:
* Testes \
├── Teste da API com Newman \
├── Teste de performance com k6
* Build/empacotamento (cria um arquivo .zip do projeto e dos relatórios gerados)
* Notification - envia e-mail ao final da pipeline

![jenkins-pipeline](https://i.imgur.com/vuK2Phj.png)

## Primeiro Build

Após subir os containers pela primeira vez, o botão "Build Now" pode não aparecer 
na interface do Jenkins. Para disparar o primeiro build manualmente via terminal:

```bash
curl -X POST http://admin:admin@localhost:8080/job/taylor-swift-api-testing-pipeline/buildWithParameters \
  --cookie-jar /tmp/cookies.txt \
  --cookie /tmp/cookies.txt \
  -H "$(curl -s --cookie-jar /tmp/cookies.txt --cookie /tmp/cookies.txt \
    http://admin:admin@localhost:8080/crumbIssuer/api/json | \
    python3 -c "import sys,json; d=json.load(sys.stdin); print(d['crumbRequestField']+':'+d['crumb'])")" \
  --data "TRIGGER=manual"
```

Após o primeiro build, o botão **"Build With Parameters"** aparecerá normalmente 
na interface do Jenkins.

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

## Imagem no Docker HUB
https://hub.docker.com/r/andradelidia/taylor-swift-jenkins


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

### Docker Hub
O Claude Sonnet 4.6 auxiliou na dúvida sobre qual imagem publicar e como realizar 
o processo de publicação, esclarecendo que o requisito exige apenas a imagem principal 
(Jenkins customizado) e que as demais já são imagens públicas do Docker Hub. 
O modelo também orientou sobre como adicionar a tag da imagem no `docker-compose.yml` 
para referenciar a imagem publicada, sem necessidade de alterar o fluxo de build.

Prompt utilizado:
> *"Como eu subo no Docker Hub a partir do compose? Preciso fazer isso mas não tenho certeza."*

A resposta esclareceu que o compose não faz push automaticamente — o push é sempre 
manual via `docker push` — e que basta adicionar a linha `image:` no serviço do 
`docker-compose.yml` para referenciar a imagem publicada.


---

### O que não foi feito por IA
- A coleção de testes do Postman foi construída manualmente, requisição por requisição
- A estrutura de organização do Docker Compose (escolha dos containers e comunicação entre eles) foi definida pelo grupo
- As decisões de arquitetura (volume compartilhado, rede bridge dedicada, separação de responsabilidades por container) foram tomadas pelo grupo
- O mapeamento dos problemas reais de execução e a validação das soluções propostas pela IA foram feitos manualmente

### Avaliação do Projeto
O Claude Sonnet 4.6 foi utilizado para realizar uma avaliação completa do projeto 
ao longo do desenvolvimento, verificando o atendimento de cada um dos 14 critérios 
do documento de projeto. A avaliação foi feita de forma iterativa, analisando os 
artefatos gerados pelo Jenkins, o `docker-compose.yml`, o `Jenkinsfile`, o `casc.yaml` 
e o histórico de commits. 

Problemas identificados e corrigidos com auxílio dessa avaliação:
- Ordem incorreta do `cp` e `zip` no stage Build (relatórios não entravam no pacote)
- Caminho inconsistente do relatório Newman entre ambiente local e container
- `archiveArtifacts` apenas no `post { success }`, impedindo o salvamento em caso de falha
- Ausência de `networks` no container nginx
- Comentário `//` no Job DSL quebrando o `casc.yaml` e removendo o botão "Build Now"
- Campo `location` no bloco errado do `casc.yaml`, impedindo o Jenkins de inicializar
- Configuração completa do webhook GitHub via `casc.yaml`, sem uso da interface gráfica

O modelo também auxiliou na configuração do webhook com ngrok, no debugging 
iterativo dos logs do Jenkins e na formatação e revisão final deste README.
