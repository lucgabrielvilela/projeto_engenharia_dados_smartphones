# 📱 Projeto de Engenharia de Dados & Governança - Mercado de Smartphones

Este projeto engloba uma pipeline ponta a ponta de **Engenharia de Dados e DataOps** para o mercado de smartphones no Brasil. O fluxo contempla a extração/geração de dados brutos em JSON, governança e dicionário de dados com SQLite, processo de ETL com validação de regras de qualidade, e visualização analítica através de um dashboard em Streamlit.

---

## 📁 Estrutura do Projeto

```text
projeto_engenharia_dados_smartphones/
│
├── src/                          # Scripts da pipeline de dados
│   ├── 1_extracao_vendas.py     # Geração e simulação da extração de vendas (JSON)
│   ├── 2_governanca_catalogo.py # Criação da estrutura do banco SQLite, catálogo e regras
│   ├── 3_etl_operacao.py        # Processamento ETL, validação de qualidade e carga
│   └── 4_dashboard_analise.py   # Dashboard analítico interativo (Streamlit)
│
├── dados_vendas/                # (Gerado na execução) Armazena os arquivos JSON de vendas
├── mercado_smartphones.db       # (Gerado na execução) Banco de dados relacional SQLite
├── .gitignore                    # Arquivos ignorados pelo Git
├── requirements.txt             # Libs Python necessárias (pandas, streamlit)
└── README.md                    # Documentação do projeto
```

---

## ⚙️ Funcionalidades & Arquitetura

1. **Extração de Vendas (`src/1_extracao_vendas.py`)**:
   - Simula a ingestão de 150 registros de vendas de smartphones no mercado brasileiro.
   - Salva cada transação individualmente como arquivo `.json` no diretório `dados_vendas/`.

2. **Governança & Catálogo (`src/2_governanca_catalogo.py`)**:
   - Define a governança no banco `mercado_smartphones.db`.
   - Cria a tabela `dicionario_dados` para metadados e documentação do schema.
   - Instancia a tabela final `vendas_celulares` com restrição de integridade `CHECK(preco_venda_brl > 0)`.
   - Instancia a tabela de logs `log_dataops` para auditoria de erros.

3. **ETL & Data Quality (`src/3_etl_operacao.py`)**:
   - Lê os arquivos JSON da pasta `dados_vendas/`.
   - Executa validações de qualidade de dados (identifica e bloqueia vendas com preços negativos/nulos).
   - Registra inconsistências detectadas no `log_dataops` e insere os registros válidos na tabela `vendas_celulares`.

4. **Dashboard Analítico (`src/4_dashboard_analise.py`)**:
   - Interface web construída com **Streamlit**.
   - Apresenta KPIs principais (Total de Vendas Válidas, Preço Médio, Marca Mais Vendida).
   - Exibe gráficos interativos por Estado (UF) e capacidade média de bateria (mAh) por modelo.

---

## 🛠️ Como Executar

### 1. Pré-requisitos
Certifique-se de ter o Python instalado. Em seguida, instale as dependências executando:

```bash
pip install -r requirements.txt
```

---

### 2. Executando a Pipeline

Execute os scripts na ordem numérica recomendada:

#### **Passo 1: Gerar os dados de vendas (JSON)**
```bash
python src/1_extracao_vendas.py
```

#### **Passo 2: Criar o banco e aplicar governança**
```bash
python src/2_governanca_catalogo.py
```

#### **Passo 3: Rodar o ETL e carga**
```bash
python src/3_etl_operacao.py
```

#### **Passo 4: Abrir o Dashboard no navegador**
```bash
streamlit run src/4_dashboard_analise.py
```

---

## 🗃️ Dicionário de Dados

| Coluna | Tipo | Descrição |
| :--- | :--- | :--- |
| `id_pedido` | TEXT | Código único da venda no e-commerce |
| `data_venda` | TEXT | Data e hora em que o cliente fechou o pedido |
| `marca` | TEXT | Fabricante do celular (Samsung, Apple, Motorola, Xiaomi) |
| `modelo` | TEXT | Nome comercial do aparelho |
| `estado_destino` | TEXT | UF do cliente (ex: PE, SP, RJ, MG, BA, CE) |
| `preco_venda_brl` | REAL | Valor final pago em Reais (Regra de Qualidade: > 0) |
| `bateria_mah` | INTEGER | Capacidade da bateria em mAh |
