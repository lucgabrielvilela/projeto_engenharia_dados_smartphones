import sqlite3

conexao = sqlite3.connect("mercado_smartphones.db")
cursor = conexao.cursor()

print("🏛️ Estruturando a Governança e o Dicionário de Dados...")

cursor.execute('''
CREATE TABLE IF NOT EXISTS dicionario_dados (
    coluna TEXT PRIMARY KEY,
    tipo TEXT,
    descricao TEXT
)
''')

dicionario = [
    ("id_pedido", "TEXT", "Código único da venda no e-commerce"),
    ("data_venda", "TEXT", "Data e hora em que o cliente fechou o pedido"),
    ("marca", "TEXT", "Fabricante do celular (Samsung, Apple, etc)"),
    ("modelo", "TEXT", "Nome comercial do aparelho"),
    ("estado_destino", "TEXT", "UF do cliente (ex: PE, SP)"),
    ("preco_venda_brl", "REAL", "Valor final pago em Reais (Regra: > 0)"),
    ("bateria_mah", "INTEGER", "Capacidade da bateria em mAh")
]
cursor.executemany("INSERT OR IGNORE INTO dicionario_dados VALUES (?, ?, ?)", dicionario)

cursor.execute('''
CREATE TABLE IF NOT EXISTS vendas_celulares (
    id_pedido TEXT PRIMARY KEY,
    data_venda TEXT NOT NULL,
    marca TEXT,
    modelo TEXT,
    estado_destino TEXT,
    preco_venda_brl REAL CHECK(preco_venda_brl > 0),
    bateria_mah INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS log_dataops (
    id_log INTEGER PRIMARY KEY AUTOINCREMENT,
    arquivo TEXT,
    erro_detectado TEXT,
    data_auditoria TEXT
)
''')

conexao.commit()
conexao.close()
print("✅ Banco 'mercado_smartphones.db' criado e regras de governança aplicadas!")
