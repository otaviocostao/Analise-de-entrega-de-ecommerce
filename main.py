import streamlit as st
import pandas as pd

st.set_page_config(page_title='Analise de entregas')

st.title('Analise de entregas do E-Commerce')
st.subheader('Dashboard')
st.write('Tabela')

tabela = pd.read_csv('ecommerceData.csv')
#st.table(tabela)

# QUANTIDADE DE PRODUTO POR GALPAO
galpoes = tabela['Warehouse_block'].value_counts()
st.table(galpoes)

# QUANTIDADE DE PRODUTO POR MEIO DE TRANSPORTE
transporte = tabela['Mode_of_Shipment'].value_counts()
st.table(transporte)

# ENTREGUE EM TEMPO POR MEIO DE TRANSPORTE
col_entregue = tabela['Reached.on.Time_Y.N'] #COLUNA 'Reached.on.Time_Y.N' 
col_transp = tabela['Mode_of_Shipment'] #COLUNA 'Mode_of_Shipment'
tab_transp = pd.DataFrame({'transporte': col_transp, 'entregue': col_entregue}) #TABELA COM 'Mode_of_Shipment' e 'Reached.on.Time_Y.N'

transp_entrega = tab_transp.groupby(['transporte']).mean()
st.table(transp_entrega)

# ENTREGUE EM TEMPO POR GALPAO
col_galpao = tabela['Warehouse_block']
tab_galpao = pd.DataFrame({'galpao': col_galpao, 'entregue': col_entregue}) #TABELA COM 'Warehouse_block' e 'Reached.on.Time_Y.N'

galpao_entrega = tab_galpao.groupby(['galpao']).mean()
st.table(galpao_entrega)