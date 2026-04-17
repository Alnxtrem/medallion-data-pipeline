# Medallion Data Pipeline with React Dashboard

Este projeto implementa um pipeline de dados completo baseado na arquitetura Medalhão (Bronze, Silver e Gold), simulando um cenário real de negócio com geração de dados sintéticos, processamento em Python e visualização em um dashboard React.

## Visão Geral

O objetivo é demonstrar um fluxo de dados ponta a ponta, desde a ingestão até o consumo analítico, seguindo boas práticas de engenharia de dados.

O pipeline inclui:

* Geração de dados sintéticos em escala
* Tratamento e padronização de dados
* Criação de métricas de negócio
* Disponibilização para consumo via frontend

## Dashboard

<img width="1600" height="899" alt="image" src="https://github.com/user-attachments/assets/78eadba1-b3bd-4e3e-beb3-fb44a8c5c2b4" />

## Gráfico de Faturamento

<img width="1600" height="899" alt="image" src="https://github.com/user-attachments/assets/c43c6757-24e8-4eee-a675-bdc8a5a21580" />

## Arquitetura

A arquitetura segue o padrão Medalhão:

* **Bronze**: dados brutos gerados, sem tratamento
* **Silver**: dados limpos, tipados e estruturados
* **Gold**: dados agregados com foco em métricas de negócio

Fluxo:

Bronze → Silver → Gold → Dashboard (React)

## Métricas Geradas

A camada Gold disponibiliza:

* Faturamento total
* Faturamento por cliente
* Faturamento mensal
* Ranking de clientes (Top N)

Essas métricas simulam indicadores utilizados em contextos reais de análise de desempenho.

## Tecnologias Utilizadas

* Python (Pandas, Faker)
* React (Frontend)
* CSV e JSON como camadas de persistência

## Estrutura do Projeto

```text
bronze/             dados brutos gerados
silver/             dados tratados e enriquecidos
gold/               dados agregados para consumo
dashboard/          exportações JSON da camada gold
dashboard-react/    aplicação React
etl/                scripts do pipeline
assets/             imagens do projeto
```

## Como Executar

### 1. Instalar dependências Python

```bash
pip install -r requirements.txt
```

### 2. Executar o pipeline de dados

```bash
python etl/generate_data.py
python etl/bronze_to_silver.py
python etl/silver_to_gold.py
```

### 3. Executar o dashboard

```bash
cd dashboard-react
npm install
npm start
```

O dashboard estará disponível em:
http://localhost:3000

## Considerações

* Os dados são sintéticos e foram gerados exclusivamente para fins de demonstração.
* O pipeline simula cenários reais, incluindo dados incompletos e necessidade de tratamento.
* O dashboard consome diretamente os arquivos JSON gerados na camada Gold.

## Objetivo do Projeto

Este projeto demonstra, na prática, conceitos essenciais de engenharia de dados:

* Arquitetura em camadas (Medalhão)
* Qualidade e tratamento de dados
* Modelagem orientada a consumo
* Integração entre backend e frontend

Serve como base para evoluções como uso de banco de dados, APIs ou orquestração de pipelines.
