import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("📊 Análise de Deputados por Partido")


df = pd.read_csv("deputados.csv")

partidos = df["partido"].value_counts()


fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(partidos.index, partidos.values, color="cornflowerblue")
ax.set_title("Número de Deputados por Partido")
ax.set_xlabel("Partido")
ax.set_ylabel("Quantidade")


st.pyplot(fig)

st.subheader("📋 Tabela de Dados")
st.dataframe(df)
