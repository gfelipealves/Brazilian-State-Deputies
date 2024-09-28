import streamlit as st
import pandas as pd
from graphics.graphics import viewAll
import plotly.express as px

# Configurar o título da página
st.set_page_config(page_title="Gastos dos Deputados Alesp", layout="wide")

# Criar a instância da classe viewAll
view = viewAll()

################## Exibir Barra Lateral #######################
# Construir o aplicativo Streamlit
st.sidebar.title("Selecione as Informações Abaixo:")

# Criar uma lista suspensa no Streamlit
selectedName = st.sidebar.selectbox("Selecione o Deputado", view.allNames())

# Criar uma lista suspensa no Streamlit
selectedYear = st.sidebar.selectbox("Selecione o Ano", view.allYears())

# Criar uma lista suspensa no Streamlit
selectedKind = st.sidebar.selectbox("Selecione o Tipo de Despesa", view.allKind())

################## Exibir Gráficos #######################
# Título
st.markdown(
    """
    <h2 style='text-align: center; font-size:20px; color:black;'>
        Gasto dos Deputados Estaduais de São Paulo
    </h2>
    """,
    unsafe_allow_html=True
)
# Exibir gráfico com maiores custos
view.filterHigherCust()

# Exibir gráfico com menores custos
view.filterLowerCust()

# Filtrar por nome
view.filterName(selectedName)

# Filtrar por nome e ano
view.filterNameYear(selectedName, selectedYear)

# Exibir a tabela com filtro
view.table(selectedName, selectedYear, selectedKind)