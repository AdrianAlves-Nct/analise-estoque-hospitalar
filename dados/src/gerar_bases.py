import pandas as pd
import numpy as np
from pathlib import Path

# Para gerar sempre os mesmos dados simulados
np.random.seed(42)

# Criando pasta dados caso ela não exista
Path("dados").mkdir(exist_ok=True)

# -----------------------------
# Base de produtos simulados
# -----------------------------

produtos = [
    ("0001", "Dipirona 500mg/mL", "Medicamento"),
    ("0002", "Soro Fisiologico 0,9% 500mL", "Solucoes"),
    ("0003", "Soro Glicosado 5% 500mL", "Solucoes"),
    ("0004", "Equipo Macrogotas", "Material Hospitalar"),
    ("0005", "Seringa 10mL", "Material Hospitalar"),
    ("0006", "Seringa 20mL", "Material Hospitalar"),
    ("0007", "Agulha 25x7", "Material Hospitalar"),
    ("0008", "Luva Procedimento M", "Material Hospitalar"),
    ("0009", "Omeprazol 40mg", "Medicamento"),
    ("0010", "Ceftriaxona 1g", "Antibiotico"),
    ("0011", "Ampicilina 1g", "Antibiotico"),
    ("0012", "Metoclopramida 10mg", "Medicamento"),
    ("0013", "Ondansetrona 4mg", "Medicamento"),
    ("0014", "Furosemida 20mg", "Medicamento"),
    ("0015", "Hidrocortisona 100mg", "Medicamento"),
    ("0016", "Adrenalina 1mg/mL", "Medicamento"),
    ("0017", "Atropina 0,25mg/mL", "Medicamento"),
    ("0018", "Cloreto de Sodio 20%", "Solucoes"),
    ("0019", "Glicose 50%", "Solucoes"),
    ("0020", "Cateter Venoso 20G", "Material Hospitalar"),
    ("0021", "Cateter Venoso 22G", "Material Hospitalar"),
    ("0022", "Mascara Cirurgica", "Material Hospitalar"),
    ("0023", "Compressa Gaze", "Material Hospitalar"),
    ("0024", "Esparadrapo", "Material Hospitalar"),
    ("0025", "Alcool 70%", "Material Hospitalar"),
]

setores = ["Urgencia", "UTI", "Bloco Cirurgico", "Clínica Médica"]

# -----------------------------
# Criando estoque_atual.csv
# -----------------------------

estoque = []

for codigo, produto, grupo in produtos:
    estoque_atual = np.random.randint(20, 1000)
    estoque_minimo = np.random.randint(30, 200)
    estoque_maximo = estoque_minimo + np.random.randint(200, 1000)
    tempo_reposicao = np.random.randint(3, 20)

    estoque.append({
        "Codigo": codigo,
        "Produto": produto,
        "Grupo": grupo,
        "Estoque_Atual": estoque_atual,
        "Estoque_Minimo": estoque_minimo,
        "Estoque_Maximo": estoque_maximo,
        "Tempo_Reposicao_Dias": tempo_reposicao
    })

df_estoque = pd.DataFrame(estoque)

df_estoque.to_csv("dados/estoque_atual.csv", index=False, encoding="utf-8-sig")

# -----------------------------
# Criando consumo_mensal.csv
# -----------------------------

datas = pd.date_range(start="2024-01-01", end="2024-06-30", freq="D")

consumo = []

for data in datas:
    # Nem todo produto será consumido todos os dias
    produtos_do_dia = np.random.choice(len(produtos), size=np.random.randint(8, 18), replace=False)

    for idx in produtos_do_dia:
        codigo, produto, grupo = produtos[idx]

        setor = np.random.choice(setores, p=[0.40, 0.25, 0.20, 0.15])

        if grupo == "Material Hospitalar":
            quantidade = np.random.randint(10, 120)
        elif grupo == "Solucoes":
            quantidade = np.random.randint(5, 80)
        elif grupo == "Antibiotico":
            quantidade = np.random.randint(1, 30)
        else:
            quantidade = np.random.randint(1, 60)

        consumo.append({
            "Data": data.strftime("%Y-%m-%d"),
            "Codigo": codigo,
            "Produto": produto,
            "Grupo": grupo,
            "Setor": setor,
            "Quantidade_Consumida": quantidade
        })

df_consumo = pd.DataFrame(consumo)

df_consumo.to_csv("dados/consumo_mensal.csv", index=False, encoding="utf-8-sig")

print("Bases simuladas criadas com sucesso!")
print(f"Arquivo estoque_atual.csv: {df_estoque.shape[0]} linhas e {df_estoque.shape[1]} colunas")
print(f"Arquivo consumo_mensal.csv: {df_consumo.shape[0]} linhas e {df_consumo.shape[1]} colunas")