# Testes da "Taylor Swift API" com Postman e Newman

Repositório dedicado à disciplina S07 - Qualidade de Software.

Integrantes:
-
Ana Luísa Galvão Valeta | 208 <br> 
Júlio César Taranto Azevedo | 454 <br> 
Lídia Carolina de Andrade Rosa | 641 <br> 
Maria Eduarda Constância Rocha Moreira | 710

O projeto utiliza a [Taylor Swift API](https://github.com/sarbor/taylor_swift_api) criada pelo usuário [*Sarbor*](https://github.com/sarbor) no Github, sendo uma AP REST pública e gratuita.
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




