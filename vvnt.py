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
st.subheader('Digite as informações ao lado')

st.sidebar.header('Informações de quantidade de açai')
dia=st.sidebar.number_input('que dia é hj',min_value=0, max_value=35)
periodo=st.sidebar.text_input('qual periodo')
t = st.sidebar.number_input('Quantos açais trandicionais',min_value=0, max_value=1000)
ada = st.sidebar.number_input('Quantos Açais adicionais completos vendidos', min_value=0, max_value=1000)
adc = st.sidebar.number_input('Quantos Açais com creme de avelã vendidos', min_value=0, max_value=1000)
adp = st.sidebar.number_input('Quantos Açais com paçoca vendidos?', min_value=0, max_value=1000)
limpeza = st.sidebar.button('Limpar dados do banco de dados')
if limpeza:
    comando = "DELETE FROM controle2"
    cursor.execute(comando)
    conexao.commit()
    st.write('Dados do banco de dados limpos com sucesso!')
st.write ('---')
tf=t*13
adaf = ada * 18
adcf = adc * 16
adpf = adp * 15
valor =  tf+adaf+adcf+adpf
if st.button('Iniciar'):
    enviar = f"INSERT INTO controle2 (dia_vendido, período, tradicional, Adicional_ambos, Adicional_creme_de_avelã, Adicional_paçoca) VALUES ({dia}, '{periodo}', {t}, {ada}, {adc}, {adp})"
    cursor.execute(enviar)
    conexao.commit()
    st.write(f'o valor constado nas vendas é de R${valor}.')
    st.write(f'A quantidade de açai Tradicional foi de {t} e o valor arrecadado foi de R${tf}')
    st.write(f'A quantidade de açai Adicional completo foi de {ada} e o valor scorecard foi de R${adaf}')
    st.write(f'A quantidade de açai Adicional creme de avelã foi de {adc} e o valor arrecadado foi de R${adcf}')
    st.write(f'A quantidade de açai Adicional com paçoca foi de {adp} e o valor arrecadado foi de R${adpf}')
    st.write(f'refentes ao dia {dia} no periodo {periodo}')
    tabela = 'Select * from controle2'
    cursor.execute(tabela)
    resultado = cursor.fetchall()
    st.write (pd.DataFrame(resultado, columns=['dia', 'periodo', 'tradicional', 'Adicional ambos', 'adicional creme de avelã', 'adicional paçoca',]))
    cursor.execute("SELECT Tradicional, Adicional_ambos, adicional_creme_de_avelã, adicional_paçoca FROM controle2")
    resultado = cursor.fetchall()
    colunas_nomes = ['Tradicional','Adicional_ambos','adicional_creme_de_avelã','adicional_paçoca']
    df = pd.DataFrame(resultado, columns=colunas_nomes)
    for col in colunas_nomes:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
    soma_total = df[colunas_nomes].sum().sum()
    st.write("Soma total de todas as colunas:", soma_total)

cursor.close()
conexao.close()