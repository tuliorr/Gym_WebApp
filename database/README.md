# Banco de dados

## Estrutura

## Acesso via Docker

* Baixar imagem do Postgres

        docker pull postgres

* Rodar contaneir 

        docker run --name dbgymapp -e POSTGRES_PASSWORD=gym123 -d -p 5432:5432 postgres