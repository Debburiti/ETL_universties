# Projeto ETL Universidades 

##Cadeira engenharia de dados e Big data | Cesar School

Este projeto realiza a extração de dados da API Hipolabs e a persistência em um banco de dados relacional SQLite, seguindo princípios de Programação Orientada a Objetos.

## Integrantes do Grupo
1. Debora Almeida Buriti da Silva
2. Mirella Emily Bezerra Santana

## Estrutura do Projeto
- `src/extract.py`: Classe de extração (API -> JSON).
- `src/load.py`: Classe de carga (JSON -> SQLite).
- `main.py`: Ponto de entrada da aplicação.

## Como Executar
1. Ative seu ambiente virtual (`venv`).
2. Instale as dependências:
   ```bash
   pip install requests black
