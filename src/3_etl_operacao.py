import os
import json
import sqlite3
from datetime import datetime

conexao = sqlite3.connect("mercado_smartphones.db")
cursor = conexao.cursor()

pasta = "dados_vendas"
arquivos = os.listdir(pasta)

sucessos = 0
rejeitados = 0

print("⚙️ Rodando ETL e validação de qualidade dos preços...")

for arquivo in arquivos:
    if arquivo.endswith(".json"):
        caminho = os.path.join(pasta, arquivo)
        
        with open(caminho, "r") as f:
            venda = json.load(f)
        
        if venda["preco_venda_brl"] <= 0:
            cursor.execute(
                "INSERT INTO log_dataops (arquivo, erro_detectado, data_auditoria) VALUES (?, ?, ?)",
                (arquivo, f"Preço inválido: R$ {venda['preco_venda_brl']}", datetime.now().isoformat())
            )
            rejeitados += 1
            continue
        
        try:
            cursor.execute('''
                INSERT INTO vendas_celulares 
                (id_pedido, data_venda, marca, modelo, estado_destino, preco_venda_brl, bateria_mah)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                venda["id_pedido"], venda["data_venda"], venda["marca"],
                venda["modelo"], venda["estado_destino"], venda["preco_venda_brl"], venda["bateria_mah"]
            ))
            sucessos += 1
        except sqlite3.IntegrityError:
            pass

conexao.commit()
conexao.close()

print(f"🎯 Carga finalizada!\n- Vendas registradas: {sucessos}\n- Erros de preço bloqueados: {rejeitados}")
