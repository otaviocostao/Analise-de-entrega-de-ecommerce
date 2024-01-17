import streamlit as st
import pandas as pd

st.set_page_config(page_title='Analise de entregas')

st.title('Analise de entregas do E-Commerce')

tabela = pd.read_csv('ecommerceData.csv')
#st.table(tabela)

st.subheader('Quantidade de produtos')
# QUANTIDADE DE PRODUTO POR GALPAO
st.write('Quantidade de produtos em cada galpão')
galpoes = tabela['Warehouse_block'].value_counts()
st.bar_chart(galpoes)

# QUANTIDADE DE PRODUTO POR MEIO DE TRANSPORTE
st.write('Quantidade de produtos em cada meio de transporte')
transporte = tabela['Mode_of_Shipment'].value_counts()
st.bar_chart(transporte)

#COMPARACAO DE ENTREGAS
st.subheader('Porcentagem de entrega no tempo prometido')

# ENTREGUE EM TEMPO POR MEIO DE TRANSPORTE
st.write('Porcentagem por meio de transporte')
col_entregue = tabela['Reached.on.Time_Y.N'] #COLUNA 'Reached.on.Time_Y.N' 
col_transp = tabela['Mode_of_Shipment'] #COLUNA 'Mode_of_Shipment'
tab_transp = pd.DataFrame({'transporte': col_transp, 'entregue': col_entregue}) #TABELA COM 'Mode_of_Shipment' e 'Reached.on.Time_Y.N'

transp_entrega = tab_transp.groupby(['transporte']).mean()
st.bar_chart(transp_entrega)

# ENTREGUE EM TEMPO POR GALPAO
st.write('Porcentagem por galpão')
col_galpao = tabela['Warehouse_block']
tab_galpao = pd.DataFrame({'galpao': col_galpao, 'entregue': col_entregue}) #TABELA COM 'Warehouse_block' e 'Reached.on.Time_Y.N'

galpao_entrega = tab_galpao.groupby(['galpao']).mean()
st.bar_chart(galpao_entrega)

# ENTREGUE EM TEMPO POR IMPORTANCIA DO PRODUTO
st.write('Porcentagem por importância do produto')
col_importancia = tabela['Product_importance']
tab_importancia = pd.DataFrame({'importancia': col_importancia, 'entregue': col_entregue})

importancia_entrega = tab_importancia.groupby(['importancia']).mean()
st.bar_chart(importancia_entrega)