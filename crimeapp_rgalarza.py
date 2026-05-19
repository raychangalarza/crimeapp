import pandas as pd
import streamlit as st
import plotly.express as px

# Title 
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

# Function for map graph
def dameIndice(delito):
  if delito == "Asesinato":
    return 10
  elif delito == "Violacion":
    return 9.5
  elif delito == "Trata Humana":
    return 9.0
  elif delito == "Incendio Malicioso":
    return 8.5
  elif delito == "Agresion Agravada":
    return 8.0
  elif delito == "Robo":
    return 7.0
  elif delito == "Escalamiento":
    return 6.0
  elif delito == "Vehiculo Hurtado":
    return 5.5
  elif delito == "Apropiacion Ilegal":
    return 5.0
  else:
    return 4
  
