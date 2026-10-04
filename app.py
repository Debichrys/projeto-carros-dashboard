import pandas as pd
import plotly.express as px
import streamlit as st

# 1. Criar um cabeçalho para a página
st.header('Dashboard de Análise de Dados de Veículos')

# 2. Ler os dados do ficheiro de carros
car_data = pd.read_csv('vehicles.csv') 

# 3. Criar caixas de seleção (checkboxes) em vez de botões
show_histogram = st.checkbox('Mostrar histograma')
show_scatter = st.checkbox('Mostrar gráfico de dispersão')

# Se a caixa do histograma estiver marcada
if show_histogram:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Se a caixa do gráfico de dispersão estiver marcada
if show_scatter:
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Relação entre Preço e Quilometragem")
    st.plotly_chart(fig_scatter, use_container_width=True)
