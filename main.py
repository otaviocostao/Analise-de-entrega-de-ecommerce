import streamlit as st
import pandas as pd

st.set_page_config(page_title='Analise de eletrônicos')

st.title('Analise de vendas de eletrônicos')
st.subheader('Dashboard das vendas por categoria')
st.write('Tabela')

tabela = pd.read_csv('ElectronicsData.csv')
sub_category= tabela['Sub Category']
price = tabela['Price']

tabela_categoria = pd.DataFrame({'Sub_Category': sub_category, 'Price': price})

st.table(tabela_categoria)
