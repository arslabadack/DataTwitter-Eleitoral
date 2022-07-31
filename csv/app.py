import pandas as pd
import streamlit as st
from PIL import Image

# image = Image.open('logo.png')
# st.image(image)

st.title('Sentimentos Presidenciaveis')


df = pd.read_csv('dataframe_final.csv')
candidato_unico = sorted(df['Candidato'].unique())
selecionar_candidato = st.sidebar.multiselect('Candidato', candidato_unico)
df_candidato_selecionado = df[(df['Candidato'].isin(selecionar_candidato))]

st.dataframe(df_candidato_selecionado)

print(candidato_unico)
