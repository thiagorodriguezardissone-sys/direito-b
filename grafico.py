import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv("deputados.csv")
partidos = df["partido"].value_counts()

plt.figure(figsize=(10,5))
partidos.plot(kind="bar", color="skyblue")
plt.title("Número de Deputados por Partido")
plt.xlabel("Partido")
plt.ylabel("Quantidade")
plt.tight_layout()
plt.show()
