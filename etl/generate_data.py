from faker import Faker
import pandas as pd
import random
import os
from datetime import datetime, timedelta

fake = Faker("pt_BR")

NUM_REGISTROS = 100000  # pode aumentar depois

dados = []

clientes = [fake.name() for _ in range(1000)]

for i in range(NUM_REGISTROS):
    # distribuição mais realista
    valor = round(abs(random.gauss(300, 150)), 2)

    # simular dado sujo
    if random.random() < 0.1:
        valor = None

    # datas ao longo de 1 ano
    base_date = datetime.now() - timedelta(days=365)
    data = base_date + timedelta(days=i % 365)

    dados.append({
        "id": i,
        "cliente": random.choice(clientes),
        "valor": valor,
        "data": data.date(),
        "status": random.choice(["pago", "pendente", "cancelado"])
    })

df = pd.DataFrame(dados)

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
bronze_path = os.path.join(base_dir, "bronze")

os.makedirs(bronze_path, exist_ok=True)

output_file = os.path.join(bronze_path, "dados.csv")
df.to_csv(output_file, index=False)

print(f"{NUM_REGISTROS} registros gerados com sucesso")
print(f"Arquivo salvo em: {output_file}")