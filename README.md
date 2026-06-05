# Testes da "Taylor Swift API" com Postman e Newman

Repositório dedicado à disciplina S07 - Qualidade de Software.

Integrantes:
-
Ana Luísa Galvão Valeta | 208 <br> 
Júlio César Taranto Azevedo | 454 <br> 
Lídia Carolina de Andrade Rosa | 641 <br> 
Maria Eduarda Constância Rocha Moreira | 710

O projeto utiliza a [Taylor Swift API](https://github.com/sarbor/taylor_swift_api) criada pelo usuário [*Sarbor*](https://github.com/sarbor) no Github, sendo uma API REST pública e gratuita.
Foi utilizada a ferramenta Newman para execução dos testes via linha de comando no terminal.

As informações sobre endpoints foram retiradas do README do repositório do autor.

Endpoints:
| Descrição | Endpoint |
|-----------|----------|
| Retorna todos os álbuns | `https://taylor-swift-api.sarbo.workers.dev/albums` |
| Retorna músicas de álbum específico | `https://taylor-swift-api.sarbo.workers.dev/albums/{albumId}` |
| Retorna todas as músicas | `https://taylor-swift-api.sarbo.workers.dev/songs` |
| Retorna uma música específica | `https://taylor-swift-api.sarbo.workers.dev/songs/{songId}` |
| Retorna a letra de uma música | `https://taylor-swift-api.sarbo.workers.dev/lyrics/{songId}` |
| Retorna N parágrafos de uma música | `https://taylor-swift-api.sarbo.workers.dev/lyrics?shouldRandomizeLyrics=true&numberOfParagraphs={number}` |

*tabela formatada em markdown pelo Copilot no VSCode*


## Tecnologias

### Postman
A coleção de teste foi criada no Postman, utilizando os scripts post-request (executados após as requisições).

### Newman
Para executar os testes no terminal, foi utilizada a ferramenta Newman. O relatório HTML foi gerado pelo newman-reporter-htmlextra.

### K6

**As ferramentas foram escolhidas conforme exemplos dados em sala de aula.**

## Pré-requisitos
* Node.js 20 ou superior
* npm (incluso no Node.js)
* k6

## Instalação

```bash
git clone "https://github.com/lidiacarolina/taylor-swift-api-testing/"

cd taylor-swift-api-testing

npm install
``` 

## Para executar os testes

Apenas executar os testes:
```bash
npm test 
```

Para executar os testes e gerar um relatório HTML:
```bash
npm run test:relatorio 
```
O relatório é gerado na raiz do projeto.

## Estrutura do Projeto
```bash
.
├── README.md
├── collections
│   └── taylor-swift-api-testing.postman_collection.json
├── package-lock.json
└── package.json

```

## Organização do projeto em grupo

Para versionamento, foi utilizado git com branches. Cada integrante criou sua própria branch, e depois foi realizado um Pull Request e merge para a branch 'develop'. Após finalização do projeto, foi feito o merge para a branch 'main'.

## Testes de performance
Como extra, foram criados testes de estresse e de carga utilizando a ferramenta K6. Ao final da execução dos testes é gerado automaticamente um relatório com detalhes sobre cada teste executado.

Teste de Carga -> O teste de carga simula 15 usuarios virtuais acessando a API durante 10 segundos visando verificar a estabilidade da API sobre carga leve. Cada um desses usuarios executa três requisições para os endpoints /albums, /songs e /lyrics.

Teste de Estresse -> Foi feita uma configuração em stages para definir uma subida controlada de carga, começando com 5 usuários e subindo de 5 em 5, visando simular um cenário real de crescimento de acessos e verificar como a API se comporta sob uma variação de carga. 

Estrutura:
```bash
.
├── reports
│   └── load-summary.html
│   └── stress-summary.html
├── load-test.js
└── stress-test.js

```

Para testar:
```bash
git checkout feature/ana-performance-tests

k6 run stress-test.js
k6 run load-test.js
```

/.