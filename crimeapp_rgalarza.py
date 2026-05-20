import pandas as pd
import streamlit as st
import plotly.express as px

# Title 
st.set_page_config(layout="wide")
st.title("Datos de Crímenes en Puerto Rico 2013-2016")
st.write("Fuente de datos: Policía de Puerto Rico")
st.divider()

# Creating dataframe
@st.cache_data
def load_data(data):
    df = pd.read_csv(data)
    return df

df = load_data("crime_processed.csv")

# Logo
st.sidebar.image("crimeapp_logo.png")
st.sidebar.divider()

# Text with summarized metrics
col1, col2, col3 = st.columns(3)

col1.metric("Cantidad de incidentes", f"{len(df):,}")

mas_frecuencia = df["Crime"].value_counts().head(1).index[0]
col2.metric("Delito más frecuente", mas_frecuencia)

mas_incidentes = df["Area"].value_counts().head(1).index[0]
col3.metric("Área con mas incidentes", mas_incidentes)

st.divider()

# Map and chart
col1, col2 = st.columns([1.5, 1.0], border=True)

CHART_HEIGHT = 500
# Map bubble colors
indice_gravedad = {
    "Asesinato": 10,
    "Violacion": 9.5,
    "Trata Humana": 9.0,
    "Incendio Malicioso": 8.5,
    "Agresion Agravada": 8.0,
    "Robo": 7.0,
    "Escalamiento": 6.0,
    "Vehiculo Hurtado": 5.5,
    "Apropiacion Ilegal": 5.0,
    "Otros":4.0
}
df["Gravedad"] = df["Crime"].map(indice_gravedad)

centro_zoom = dict(lat=18.25178, lon=-66.254513)
mapa_puntos = px.scatter_map(df, lat="Lat", lon="Lon", color="Gravedad", size="Gravedad", size_max=5, 
                             color_continuous_scale=px.colors.sequential.Hot_r,  height=CHART_HEIGHT, zoom=8, center=centro_zoom, 
                             map_style="carto-darkmatter-nolabels", opacity=0.3)
col1.plotly_chart(mapa_puntos, use_container_width=True)

cant = df["Crime"].value_counts().reset_index()
cant.columns = ["Crimen", "Cantidad"]

distribucion_del = px.bar(cant, x="Cantidad", y="Crimen", height=CHART_HEIGHT)
col2.plotly_chart(distribucion_del)

# Sidebar selectbox and multiselect
area_policiaca = st.sidebar.selectbox(
  "Area Policíaca", 
  ["Todas las áreas", *df["Area"].unique()]
  )

st.sidebar.divider()

delitos = st.sidebar.multiselect(
  "Delitos",
  df["Crime"].unique().tolist(),
  default=df["Crime"].unique().tolist()
)

st.sidebar.divider()

dow = st.sidebar.multiselect(
  "Día de la Semana",
  df["DOW_Name"].unique().tolist(),
  default=df["DOW_Name"].unique().tolist()
)

st.sidebar.divider()

am_pm = st.sidebar.selectbox(
  "AM ó PM",
  ["Ambas", "AM", "PM"]
)

st.sidebar.divider()

#Sidebar text
st.sidebar.write("""
Aplicación desarrollada por:\n
Raychan J. Galarza Rodríguez\n
Proyecto Final Comp3082 – Mayo 2026\n
Ciencia de Datos\n              
Universidad de Puerto Rico en Humacao
""")
