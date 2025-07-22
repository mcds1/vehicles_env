import streamlit as st
import pandas as pd
import plotly.express as px

# Título do app
st.header("Análise Exploratória de Vendas de Veículos")

# Carregar os dados (importante: caminho relativo correto)
car_data = pd.read_csv('vehicles_us.csv')

# Caixa de seleção para histograma
if st.checkbox('Mostrar histograma da quilometragem'):
    st.write("Histograma para 'odômetro'")
    fig_hist = px.histogram(car_data, x='odometer',
                            title='Distribuição da Quilometragem')
    st.plotly_chart(fig_hist, use_container_width=True)

# Caixa de seleção para gráfico de dispersão
if st.checkbox('Mostrar gráfico de dispersão (preço vs odômetro)'):
    st.write("Gráfico de dispersão: Preço vs Quilometragem")
    fig_scatter = px.scatter(car_data, x='odometer',
                             y='price', title='Preço vs Quilometragem')
    st.plotly_chart(fig_scatter, use_container_width=True)
