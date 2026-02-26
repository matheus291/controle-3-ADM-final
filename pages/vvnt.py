import streamlit as st
import pandas as pd
import pymysql

conexao = pymysql.connect(
    host="switchyard.proxy.rlwy.net",
    user="root",
    password="gKCmTIvbsijMMuhLYFnyTLCSdBqPHkma",
    database="railway",
    port=int("43734"),
    ssl={'ssl': {}}
    )


cursor = conexao.cursor()



st.set_page_config(page_title='Informações sobre a venda de açai')
st.title('venda açai 3º ADM')
st.header('Informações de quantidade de açai')
dia=st.number_input('que dia é hj',min_value=0, max_value=35)
periodo=st.text_input('qual periodo')
t = st.number_input('Quantos açais trandicionais',min_value=0, max_value=1000)
ada = st.number_input('Quantos Açais adicionais completos vendidos', min_value=0, max_value=1000)
adc = st.number_input('Quantos Açais com creme de avelã vendidos', min_value=0, max_value=1000)
adp = st.number_input('Quantos Açais com paçoca vendidos?', min_value=0, max_value=1000)
limpeza = st.sidebar.button('Limpar dados do banco de dados')
if limpeza:
    comando = "DELETE FROM controle2"
    cursor.execute(comando)
    conexao.commit()
    st.write('Dados do banco de dados limpos com sucesso!')
if st.button('enviar dados'):
    enviar= f"INSERT INTO controle2 (dia_vendido, periodo, tradicional, Adicional_ambos, Adicional_creme_de_avelã, Adicional_paçoca) VALUES ({dia},'{periodo}',{t},{ada},{adc},{adp})"
    cursor.execute(enviar)
    conexao.commit()

cursor.close()
conexao.close()