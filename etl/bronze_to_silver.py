import pandas as pd
import os

# caminho base do projeto
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

bronze_file = os.path.join(base_dir, "bronze", "dados.csv")
silver_path = os.path.join(base_dir, "silver")

os.makedirs(silver_path, exist_ok=True)

print("Lendo dados Bronze...")
df = pd.read_csv(bronze_file)

print(f"Registros iniciais: {len(df)}")

# =========================
# LIMPEZA
# =========================

# remover registros sem valor
df = df.dropna(subset=["valor"])

# garantir tipo correto
df["valor"] = pd.to_numeric(df["valor"], errors="coerce")

# remover valores inválidos
df = df[df["valor"] > 0]

# padronizar status
df["status"] = df["status"].str.lower().str.strip()

# converter data
df["data"] = pd.to_datetime(df["data"], errors="coerce")

# remover datas inválidas
df = df.dropna(subset=["data"])

# =========================
# ENRIQUECIMENTO
# =========================

# criar coluna de ano e mês
df["ano"] = df["data"].dt.year
df["mes"] = df["data"].dt.month

print(f"Registros após limpeza: {len(df)}")

# =========================
# SALVAR
# =========================

output_file = os.path.join(silver_path, "dados_tratados.csv")
df.to_csv(output_file, index=False)

print(f"Silver salvo em: {output_file}")