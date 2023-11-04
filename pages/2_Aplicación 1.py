import streamlit as st
import pandas as pd


# Diseño personalizado
st.header("Filtro 1 - resultado por comunas")

df = pd.read_csv('historico.csv')

comunas = df.loc[:,"comuna"].unique()

comuna = st.selectbox('comunas',comunas)

informacionComuna = df[df["comuna"] == comuna]

puntajesGlobals = informacionComuna.loc[:,["codigo_dane","puntaje_global"]]

st.bar_chart(puntajesGlobals.set_index('codigo_dane'))


st.header("Filtro 2 - ")

df = pd.read_csv('historico.csv')
