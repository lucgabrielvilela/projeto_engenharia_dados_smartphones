import streamlit as st
import pandas as pd
import sqlite3

conexao = sqlite3.connect("mercado_smartphones.db")
df = pd.read_sql_query("SELECT * FROM vendas_celulares", conexao)

st.title("📊 Panorama do Mercado de Smartphones - Brasil")
st.write("Análise de vendas, preços e especificações dos aparelhos mais populares.")

col1, col2, col3 = st.columns(3)
col1.metric("Total de Vendas Válidas", len(df))
col2.metric("Preço Médio (R$)", f"R$ {df['preco_venda_brl'].mean():.2f}")
if not df.empty:
    col3.metric("Marca mais vendida", df['marca'].mode()[0])

st.divider()

st.subheader("📍 Volume de Vendas por Estado (UF)")
vendas_uf = df['estado_destino'].value_counts()
st.bar_chart(vendas_uf)

st.subheader("🔋 Capacidade de Bateria por Modelo")
st.write("Média de bateria em mAh oferecida pelos modelos vendidos.")
bateria_modelo = df.groupby("modelo")["bateria_mah"].mean()
st.bar_chart(bateria_modelo)

conexao.close()
