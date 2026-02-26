import streamlit as st
import pymysql
import pandas as pd
st.title('informações abaixo')
conexao = pymysql.connect(
    host="switchyard.proxy.rlwy.net",
    user="root",
    password="gKCmTIvbsijMMuhLYFnyTLCSdBqPHkma",
    database="railway",
    port=int("43734"),
    ssl={'ssl': {}}
    )


cursor = conexao.cursor()

cursor.execute('SELECT * FROM controle2')
dados = cursor.fetchall()
colunas = [desc[0] for desc in cursor.description]

df = pd.DataFrame(dados, columns=colunas)



st.title("Tabela de Vendas")
dia_selecionado = st.selectbox('Selecione o dia', df['dia_vendido'].unique())
df_filtrado = df[df['dia_vendido']== dia_selecionado]
st.dataframe(df_filtrado)

cursor.execute("""
    SELECT 
        IFNULL(SUM(tradicional),0) +
        IFNULL(SUM(Adicional_ambos),0) +
        IFNULL(SUM(Adicional_creme_de_avelã),0) +
        IFNULL(SUM(Adicional_paçoca),0)
    FROM controle2
""")

total = cursor.fetchone()[0] or 0
st.metric("Soma Total", total)


cursor.close()
conexao.close()