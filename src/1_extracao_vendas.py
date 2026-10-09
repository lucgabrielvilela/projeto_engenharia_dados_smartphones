import json
import random
import os
from datetime import datetime, timedelta

os.makedirs("dados_vendas", exist_ok=True)

# Aparelhos mais populares no mercado brasileiro
modelos = [
    {"marca": "Samsung", "modelo": "Galaxy A56 5G", "bateria_mah": 5000},
    {"marca": "Motorola", "modelo": "Moto G84", "bateria_mah": 5000},
    {"marca": "Xiaomi", "modelo": "Redmi Note 13", "bateria_mah": 5000},
    {"marca": "Apple", "modelo": "iPhone 13", "bateria_mah": 3227}
]

estados_br = ["PE", "SP", "RJ", "MG", "BA", "CE"]

print("🛒 Gerando dados de vendas de smartphones no Brasil...")

for i in range(1, 151):
    aparelho = random.choice(modelos)
    
    dados_venda = {
        "id_pedido": f"PED-BR-{i:05d}",
        "data_venda": (datetime.now() - timedelta(days=random.randint(0, 30))).isoformat(),
        "marca": aparelho["marca"],
        "modelo": aparelho["modelo"],
        "estado_destino": random.choice(estados_br),
        "bateria_mah": aparelho["bateria_mah"],
        "preco_venda_brl": round(random.uniform(-100.0, 4500.0), 2)
    }
    
    with open(f"dados_vendas/venda_{i:04d}.json", "w") as f:
        json.dump(dados_venda, f, indent=4)

print("✨ Sucesso! 150 registros de vendas gerados na pasta 'dados_vendas'.")
