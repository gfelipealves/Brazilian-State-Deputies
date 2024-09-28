# Avaliação dos Gastos dos Deputados Estaduais de São Paulo

Este projeto utiliza uma aplicação Streamlit para analisar e visualizar os gastos dos Deputados Estaduais do estado de São Paulo.

## O que este projeto cobre?
- **Coleta de Dados**: Dados são obtidos a partir de um arquivo XML disponível no repositório da Alesp, que contém informações sobre as despesas dos gabinetes dos deputados desde 2015.
- **Análise dos Dados**: O projeto permite filtrar e visualizar os gastos dos deputados, categorizando-os por ano, tipo de despesa e mais.
- **Visualizações**: Gráficos interativos são gerados com Plotly, mostrando os 20 deputados que mais e menos gastaram, além de análises específicas de gastos por deputado e ano.
- **Tabelas Dinâmicas**: Permite a visualização detalhada das despesas, com a opção de filtrar por mês e tipo de despesa.

Esta é uma oportunidade para explorar como os deputados estaduais utilizam os recursos públicos, promovendo maior transparência e responsabilidade fiscal.

## Instruções
Para executar a aplicação, use o comando:
```bash
streamlit run main.py


Informações gerais:
1. O que é o projeto Dados Abertos ALESP?
O Portal Dados Abertos ALESP é a ferramenta disponibilizada pelo parlamento paulista para que todos possam encontrar e utilizar os dados e as informações públicas da casa. O portal também tem o objetivo de promover a interlocução entre atores da sociedade e os seus representantes para pensar a melhor utilização dos dados em prol de uma sociedade melhor.


2. Quais dados estão disponíveis aqui?
O portal tem o objetivo de disponibilizar todo e qualquer tipo de dado relativo ao Poder Legislativo do Estado de São Paulo. Por exemplo, dados do Processo Legislativo, informações sobre os deputados estaduais (contatos, áreas de atuação, bases eleitorais, produção legislativa), da prestação de contas dos deputados com os gastos de gabinetes, etc. O portal funciona como um grande catálogo que facilita a busca e uso de dados produzidos e publicados pela ALESP.

3. Porque a ALESP está abrindo os seus dados?
O acesso a informação está previsto na Constituição Federal e na Declaração Universal dos Direitos Humanos e a Transparência é um dos pilares das ações da Mesa Diretora da Assembleia Legislativa do Estado de São Paulo. Em 18 de novembro de 2011, foi sancionada a Lei de Acesso a Informação Pública (Lei 12.527/2011) que regula o acesso a dados e informações públicas. Entre os diversos requisitos técnicos explicitados por essa lei, há um que exige que a informação solicitada pelo cidadão deve seguir critérios tecnológicos alinhados com os princípios dos Dados Abertos Governamentais. Dentro desse contexto, o Portal dos Dados Abertos Alesp é a ferramenta construída pelo parlamento estadual paulista para centralizar a busca e o acesso dos dados e informações públicas.

Lei de Acesso à Informação
A Lei de Acesso à Informação Pública (LAI)
Reconhecido como um direito humano fundamental, o acesso à informação sob a guarda de órgãos e entidades governamentais está inscrito em diversas convenções e tratados internacionais assinados pelo Brasil. Esse direito fundamental também é reconhecido por importantes organismos da comunidade internacional, como a Organização das Nações Unidas (ONU).

É também definido pela Constituição Federal de 1988, em seu no art. 5º, inciso XIV, como direito fundamental do cidadão brasileiro e um dever do Estado: Todos têm direito a receber dos órgãos públicos informações de seu interesse particular, ou de interesse coletivo ou geral, que serão prestadas no prazo da lei, sob pena de responsabilidade, ressalvadas aquelas cujo sigilo seja imprescindível à segurança da sociedade e do Estado (BRASIL. 1988, art. 5º).

A Lei nº 12.527, apelidada de Lei de Acesso à Informação (LAI), sancionada em 18 de novembro de 2011, tem o propósito de regulamentar esse direito constitucional de acesso dos cidadãos às informações públicas. Devem cumprir a LAI os órgãos públicos dos três Poderes de Estado (Executivo, Legislativo e Judiciário) de todos os níveis de governo (federal, estadual, distrital e municipal), os Tribunais de Contas e o Ministério Público, bem como as autarquias, fundações públicas, empresas públicas, sociedades de economia mista e demais entidades controladas direta ou indiretamente pela União, Estados, Distrito Federal e Municípios.

O Estado de São Paulo e o seu Parlamento - a Assembleia Legislativa do Estado de São Paulo (ALESP) - também devem, portanto, atender aos comandos especificados nessa norma. A lei obriga os órgãos públicos a publicarem seus dados em sítios oficiais na internet (LAI - Artigo 8º, § 2º) e estes deverão atender aos seguintes requisitos (LAI - Artigo 8º, § 3º):


O site deve ter uma ferramenta de pesquisa de conteúdo;
Indicar meios de contato por via eletrônica ou telefônica com o órgão que mantém o site;
Deve ser possível realizar o download das informações em formato eletrônico (planilhas e texto);
O site deve ser aberto à ação de mecanismos automáticos de recolhimento de informações, em formatos abertos e estruturados ;
A autenticidade e a integridade das informações do site devem ser garantidas pelo órgão;
Manter atualizadas as informações disponíveis para acesso.

