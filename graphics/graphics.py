import requests
import pandas as pd
import plotly.express as px
import streamlit as st
import json


withGraphic= 600
heightGraphic = 600 
# Site da Alesp com os dados
class dataBase:
    @st.cache_data
    def getData():
        URL = 'https://www.al.sp.gov.br/repositorioDados/deputados/despesas_gabinetes.xml'
        # Conexão
        Conexao = requests.get(URL)
        Base_Deputados = pd.read_xml(Conexao.content)
        Base_Deputados = Base_Deputados.query('Ano >= 2010')
        return Base_Deputados

class viewAll:
    def __init__(self):
        self.Base_Deputados = dataBase.getData() # Carregar os dados uma vez

    def allNames(self):
        # Retorna a lista de nomes únicos dos deputados
        allNames = self.Base_Deputados['Deputado'].drop_duplicates().sort_values(ascending=True).tolist()
        return allNames
    
    def allYears(self):
        # Retorna a lista de tipos únicos de anos
        allYears = self.Base_Deputados['Ano'].drop_duplicates().sort_values(ascending=True).tolist()
        return allYears
    
    def allKind(self):
        # Retorna a lista de tipos de serviços
        allKinds = self.Base_Deputados['Tipo'].drop_duplicates().sort_values(ascending=True).tolist()
        return allKinds
    
    def filterHigherCust(self):
        # Filtar o maior custo
        deputadosMaiorCusto = self.Base_Deputados[['Deputado', 'Valor', 'Ano']].groupby(by=['Deputado', 'Ano']).sum().sort_values(by=['Valor'], ascending=False).head(20).reset_index()

        # Criar uma coluna temporária que desambigua os valores duplicados
        deputadosMaiorCusto['Deputado'] = deputadosMaiorCusto['Deputado'] + " (" + deputadosMaiorCusto['Ano'].astype(str) + ")"

        # Criar o gráfico
        fig = px.bar(deputadosMaiorCusto.sort_values(by='Valor', ascending=True),
                    x='Valor',
                    y='Deputado',
                    orientation='h',
                    text='Ano',
                    template='plotly',
                    width=withGraphic, height=heightGraphic,
                    title="Os 20 Deputados que mais gastaram"
                    )
        # Título a esquerda
        fig.update_layout(title_x=0)
        
        # Apresentar o gráfico no Streamlit
        st.plotly_chart(fig)

    def filterLowerCust(self):
        # Filtar o menor custo
        deputadosMenorCusto = self.Base_Deputados[['Deputado', 'Valor', 'Ano']].query('Ano >=2015 & Ano <= 2023').groupby(by=['Deputado', 'Ano']).sum().sort_values(by=['Valor'], ascending=True).head(20).reset_index()

        # Criar uma coluna temporária que desambigua os valores duplicados
        deputadosMenorCusto['Deputado'] = deputadosMenorCusto['Deputado'] + " (" + deputadosMenorCusto['Ano'].astype(str) + ")"

        # Criar o gráfico
        fig = px.bar(deputadosMenorCusto.sort_values(by='Valor', ascending=False),
                    x='Valor',
                    y='Deputado',
                    orientation='h',
                    text='Ano',
                    template='plotly',
                    width=withGraphic, height=heightGraphic,
                    title="Os 20 Deputados que menos gastaram de 2015 a 2023"
                    )
        # Título a esquerda
        fig.update_layout(title_x=0)

        # Apresentar o gráfico no Streamlit
        st.plotly_chart(fig)

    def filterName(self, name):
        # Filtrar por nome o Deputado e os valores gastos por ano
        pesquisaDeputado = self.Base_Deputados[['Deputado', 'Ano', 'Valor']].query(f"Deputado == '{name}'").groupby(by=['Deputado', 'Ano']).sum().sort_values(by='Ano', ascending=True).reset_index()
        # Criar o gráfico
        fig = px.bar(pesquisaDeputado.sort_values(by='Ano', ascending=False),
                    x='Ano',
                    y='Valor',
                    orientation='v',
                    text='Ano',
                    template='plotly',
                    width=withGraphic, height=heightGraphic,
                    title=f"Gasto do(a) Deputado(a) {name} nos anos em que atuou"
                    )
        # Título a esquerda
        fig.update_layout(title_x=0)

        # Apresentar o gráfico no Streamlit
        st.plotly_chart(fig)
        
    def filterNameYear(self, name, year):
        # Filtrar por nome e ano Deputado e os valores gastos por tipo de atividade
        pesquisaDeputadoAno = self.Base_Deputados[['Deputado', 'Ano', 'Tipo', 'Fornecedor', 'CNPJ', 'Valor']].query(f"Deputado == '{name}' & Ano == {year}").groupby(by=['Deputado', 'Ano', 'Tipo']).sum().sort_values(by='Valor', ascending=False).reset_index()

        # Criar o gráfico
        fig = px.bar(pesquisaDeputadoAno.sort_values(by='Valor', ascending=True),
                    x='Valor',
                    y='Tipo',
                    orientation='h',
                    text='Ano',
                    template='plotly',
                    width=withGraphic, height=heightGraphic,
                    title=f"Gasto do(a) Deputado(a) {name} no ano {year}"
                    )
        # Título a esquerda
        fig.update_layout(title_x=0)

        # Apresentar o gráfico
        st.plotly_chart(fig)

        # Gráfico de pizza
        fig = px.pie(pesquisaDeputadoAno, 
                    names='Tipo', 
                    values='Valor',
                    template='plotly',
                    title=f"Porcentagem por tipo de gasto do Deputado(a) {name} no ano {year}"
                    )

        # Título a esquerda
        fig.update_layout(title_x=0)

        # Apresentar o gráfico
        st.plotly_chart(fig)
    
    def table(self, name, year, kind):
        # Título
        st.markdown(f"<h2 style='font-size:20px; color:black;'>Tabela com os dados do(a) {name} no ano de {year} e pelo tipo de serviço {kind}</h2>", unsafe_allow_html=True)
        # Filtrar por nome e ano Deputado e os valores gastos por tipo de atividade
        pesquisaDeputadoAnoTipo = self.Base_Deputados[['Deputado', 'Ano', 'Mes', 'Tipo', 'Fornecedor', 'CNPJ', 'Valor']].query(f"Deputado == '{name}' & Ano == {year} & Tipo == '{kind}'").groupby(by=['Deputado', 'Ano', 'Mes','Tipo']).sum().sort_values(by='Mes', ascending=True)
        st.dataframe(pesquisaDeputadoAnoTipo)
        # Título
        st.markdown(f"<h2 style='font-size:20px; color:black;'>Tabela com todos os dados do(a) {name}</h2>", unsafe_allow_html=True)
        # Exibir todos os dados
        pesquisaDeputadoAnoTipoAll = self.Base_Deputados[['Deputado', 'Ano', 'Mes', 'Tipo', 'Fornecedor', 'CNPJ', 'Valor']].query(f"Deputado == '{name}'").sort_values(by=['Ano','Mes'], ascending=True)
        st.dataframe(pesquisaDeputadoAnoTipoAll)
