import os

import pandas as pd


def export_json(dataframe, filename, target_directories):
    for target_directory in target_directories:
        dataframe.to_json(
            os.path.join(target_directory, filename),
            orient="records",
            double_precision=2
        )


# caminho base
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

silver_file = os.path.join(base_dir, "silver", "dados_tratados.csv")
gold_path = os.path.join(base_dir, "gold")
dashboard_path = os.path.join(base_dir, "dashboard")
frontend_data_path = os.path.join(base_dir, "dashboard-react", "public", "data")

os.makedirs(gold_path, exist_ok=True)
os.makedirs(dashboard_path, exist_ok=True)
os.makedirs(frontend_data_path, exist_ok=True)

print("Lendo dados Silver...")
df = pd.read_csv(silver_file)

print(f"Registros recebidos: {len(df)}")

# as metricas do dashboard consideram apenas receita realizada
df["status"] = df["status"].str.lower().str.strip()
df_pago = df[df["status"] == "pago"].copy()

print(f"Registros pagos considerados no Gold: {len(df_pago)}")

# =========================
# METRICAS
# =========================

# faturamento total
faturamento_total = df_pago["valor"].sum()

# faturamento por cliente
faturamento_cliente = (
    df_pago.groupby("cliente")["valor"]
    .sum()
    .reset_index()
    .sort_values(by="valor", ascending=False)
)

# faturamento por mes
faturamento_mensal = (
    df_pago.groupby(["ano", "mes"])["valor"]
    .sum()
    .reset_index()
    .sort_values(by=["ano", "mes"])
)

# top 10 clientes
top_clientes = faturamento_cliente.head(10).copy()

faturamento_cliente["valor"] = faturamento_cliente["valor"].round(2)
faturamento_mensal["valor"] = faturamento_mensal["valor"].round(2)
top_clientes["valor"] = top_clientes["valor"].round(2)

print(f"Faturamento total: {faturamento_total:.2f}")

# =========================
# SALVAR CSV
# =========================

faturamento_cliente.to_csv(
    os.path.join(gold_path, "faturamento_cliente.csv"),
    index=False
)
faturamento_mensal.to_csv(
    os.path.join(gold_path, "faturamento_mensal.csv"),
    index=False
)
top_clientes.to_csv(os.path.join(gold_path, "top_clientes.csv"), index=False)

# =========================
# EXPORTAR JSON
# =========================

json_targets = [dashboard_path, frontend_data_path]

export_json(faturamento_cliente, "faturamento_cliente.json", json_targets)
export_json(faturamento_mensal, "faturamento_mensal.json", json_targets)
export_json(top_clientes, "top_clientes.json", json_targets)

print("Gold gerado com sucesso")
