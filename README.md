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
Como extra, foram criados testes de estresse e de carga utilizando a ferramenta K6.
[...]

Para testar:
```bash
git checkout feature/ana-performance-tests

k6 run stress-test.js
k6 run load-test.js
```

Os relatórios criados podem ser acessados na pasta "reports".

## Referências e utilização de IA

Para criação dos testes e desenvolvimento do plano de testes, foram consultadas as seguintes fontes:

[Medium - Técnica de Teste — Particionamento de Equivalência](https://medium.com/revista-tspi/t%C3%A9cnica-de-teste-particionamento-de-equival%C3%AAncia-d32a7d689d82) \
[Black Box Testing - Software Engineering](https://www.geeksforgeeks.org/software-testing/software-engineering-black-box-testing/) \
[Stack Overflow: Postman test automation - verify json array response](https://stackoverflow.com/questions/63618247/postman-test-automation-verify-json-array-response) \
[Postman Learning: Install and run Newman](https://learning.postman.com/docs/collections/using-newman-cli/installing-running-newman) \
[Grafana k6 Documents](https://grafana.com/docs/k6/latest/) \
Material de aula

Foi utilizado o Claude para execução das seguintes tarefas:
- Dentro do Postman, foi utilizado o agente de IA na versão Opus 4.6 para automatização da criação de identificadores únicos para os testes
- Também dentro do Postman, foi solicitada uma avaliação da cobertura dos testes, obtendo a seguinte resposta:

### Functional Test Coverage Analysis — taylor-swift-api-testing

#### Overview

- **Total Requests:** 12 (11 GET, 1 DELETE)
- **Total Tests:** 36
- **Test Naming Convention:** `T1xx` = positive/happy path tests, `T2xx` = negative/error tests
- **API Base URL:** `{{baseURL}}` (Taylor Swift API)
- **Pre-request Scripts:** None
- **Custom Headers / Request Bodies:** None

---

#### Endpoint Coverage

| Endpoint | Method | Requests Covering It |
|---|---|---|
| `/albums` | GET | 1 (list all albums) |
| `/albums/{id}` | GET | 2 (valid ID + non-existent ID) |
| `/albums/{id}` | DELETE | 1 (unauthorized delete) |
| `/songs` | GET | 3 (all songs, Eras Tour setlist, London Boy) |
| `/songs/{id}` | GET | 1 (invalid param `abc`) |
| `/lyrics` | GET | 3 (random with paragraphs, missing paragraphs, invalid params) |
| `/lyrics/{id}` | GET | 1 (text instead of ID) |

---

#### Test Type Breakdown

| Test Category | Count | Test IDs |
|---|---|---|
| **Status code validation** | 12 | T101, T108, T115, T117, T119, T121, T201, T205, T207, T209, T211, T213 |
| **Response format (JSON)** | 3 | T102, T109, T202 |
| **Response structure (array/object)** | 3 | T103, T110, T203 |
| **Data count/length** | 3 | T104, T111, T122 |
| **Property existence** | 4 | T105, T112, T116, T120 |
| **Specific data validation** | 5 | T106, T107, T113, T114, T118 |
| **Error message/content** | 4 | T204, T208, T210, T212 |
| **Input validation (negative)** | 2 | T206, T214 |

---

#### Strengths

1. **Good positive/negative split:** 22 positive tests (T1xx) and 14 negative tests (T2xx) — a healthy ratio.
2. **Boundary & invalid input testing:** Tests cover non-existent IDs (`/albums/999`), text instead of numeric IDs (`/songs/abc`, `/lyrics/letras`), and invalid query params (`batata`, `-5`).
3. **Data integrity checks:** Tests verify specific data values (e.g., Anti-Hero's `song_id` is 157, Midnights release date, Eras Tour setlist completeness).
4. **Consistent test ID convention:** Makes it easy to trace and report failures.

---

#### Gaps & Recommendations

| Gap | Details | Suggestion |
|---|---|---|
| **No POST/PUT/PATCH coverage** | Only GET and DELETE are tested. No create or update operations. | Add tests for creating/updating albums, songs, or lyrics if the API supports it. |
| **Missing response time checks** | No performance assertions. | Add `pm.expect(pm.response.responseTime).to.be.below(2000)` to critical endpoints. |
| **No response header validation** | Content-Type, CORS headers, etc. are not checked. | Add `pm.response.to.have.header("Content-Type", "application/json")`. |
| **No schema validation** | Response body structure is loosely checked (property existence only). | Use `pm.expect(tv4.validate(jsonData, schema))` or `ajv` for JSON schema validation. |
| **Sparse tests on some requests** | 6 requests have only 2 tests each, while 2 requests have 7 tests. | Add JSON format checks and structure assertions to the lighter requests. |
| **No collection-level scripts** | Both collection-level pre-request and test scripts are empty. | Add shared assertions (e.g., response time, content-type) at the collection level to apply to all requests. |
| **No `/lyrics/{id}` happy path** | There's a negative test for lyrics by ID, but no positive test fetching a valid lyric by ID. | Add a request like `GET /lyrics/1` with validation. |
| **No `/songs/{id}` happy path** | Only the invalid param test exists for a specific song. | Add a request like `GET /songs/157` to validate fetching a single song. |
| **No pre-request scripts** | No dynamic data setup or variable chaining. | Consider using pre-request scripts to set up test data or chain requests (e.g., fetch an album ID, then use it in the next request). |

---

#### Coverage Score: ~65%

The collection has solid foundational coverage for the main list endpoints and good negative testing, but it is missing happy-path tests for individual resource endpoints (`/songs/{id}`, `/lyrics/{id}`), write operations, response schema validation, and performance checks.

* Também foi gerada a tabela de descrição de testes do plano de testes a partir do JSON da collection com a versão Sonnet 4.6 via website
