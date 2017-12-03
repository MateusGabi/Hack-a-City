# Hack-a-City
Repositório da Equipe 5⃣🦊. O objetivo do nosso software é a prevenção de crimes em Campo Grande - MS. A aplicação se consiste em quatro frentes de trabalho (módulos).

- Banco de Dados NoSQL com Servico REST integrado.
- Camada de Serviço com as Regras de Negócio no padrão REST.
- Aplicação Web.
- Aplicação Mobile.

## Banco de Dados

O Banco de Dados escolhido foi o ElasticSearch, que é OpenSource (Licença Apache-2.0), Distribuido e NoSQL. O código fonte do ElasticSearch encontra-se no [GitHub](https://github.com/elastic/elasticsearch).

### Instalação

- [Baixe](https://github.com/elastic/elasticsearch/releases) a versão mais recente e descompacte.
- Execute `bin/elasticsearch` no Unix, ou `bin\elasticsearch.bat` no Linux.
- Execute `curl -X GET http://localhost:9200/`.

## Serviço

O serviço contendo as regras de negócio  da aplicação foi desenvolvido em Python, com o [Framework Flask](https://github.com/pallets/flask/). Flask é de fácil uso e seu desenvolvimento é rápido.

### Instalação e Execução

- Entre nas pasta:
    - `cd backend`
- Baixe os pacotes:
    - `pip install flask`
    - `pip install flask_restful`
    - `pip install flask_cors`
    - `pip install es_sql`
    - `pip install datetime`
- Execute o main:
    - `python api.py`
- Execute:
    - `curl -X GET http://localhost:5000/info`

## Aplicação Web

A aplicação cliente foi desenvolvida utilizando os Frameworks Angular 2 e Material Design Lite respectivamente para as estruturas lógicas e layout.

### Instalação

Para a utiliação do aplicativo cliente é necessário ter o [Angular CLI](https://github.com/angular/angular-cli) instalado.

- Angular CLI instalado
- Execute `npm install` e `ng serve`
- Acesse http://localhost:4200

## Aplicação Mobile

Infelizmente não foi desenvolvido a versão mobile.
