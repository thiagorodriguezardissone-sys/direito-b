import pandas as pd
import streamlit as st

dataset = pd.read_csv("https://www.irdx.com.br/media/uploads/paises.csv")

import plotly.express as px

fig = px.scatter_geo(dataset,
                     lat=dataset["latitude"],
                     lon=dataset["longitude"],
                     hover_name=dataset["nome"])
fig.update_layout(title="Coordenadas dos Países no Mapa",
                  geo_scope= "world")
fig.show()
