# Medallion Pipeline Demo

Projeto de portfólio com arquitetura medalhão usando dados sintéticos, ETL em Python e dashboard em React.

## O que este projeto mostra

- Geração de dados fakes com clientes, datas, status e valores.
- Tratamento na camada `silver` com limpeza e padronização.
- Agregações na camada `gold` para faturamento mensal, ranking de clientes e visão executiva.
- Dashboard React consumindo os JSONs publicados automaticamente em `dashboard-react/public/data`.

## Estrutura

```text
bronze/         dados brutos gerados
silver/         dados tratados
gold/           agregacoes finais em CSV
dashboard/      exportacao JSON da camada gold
dashboard-react/ front-end do dashboard
etl/            scripts do pipeline
```

## Como rodar

### 1. Instalar dependências Python

```bash
pip install -r requirements.txt
```

### 2. Executar o pipeline

```bash
python etl/generate_data.py
python etl/bronze_to_silver.py
python etl/silver_to_gold.py
```

### 3. Subir o front-end

```bash
cd dashboard-react
npm install
npm start
```

## Observações

- O dashboard usa apenas transações com `status = pago` para calcular receita.
- Os arquivos JSON consumidos pelo React são atualizados na etapa `silver_to_gold.py`.
- Os dados e análises são sintéticos e servem apenas para demonstração.
