
import streamlit as st

pg = st.navigation([
    st.Page('manual.py',title='manual'),
    st.Page('vvnt.py', title='tabela'),
    st.Page('resultados.py', title='resultados')
])

pg.run()