import pandas as pd
import streamlit as st
import plotly.express as px

# Title 
st.logo("crimeapp_logo.png", size='large')
st.title("Dashboard de Datos de Crímenes en Puerto Rico")

# Creating dataframe
@st.cache_data
def load_data(data):
    df = pd.read_csv(data)
    return df

df = load_data("crime_processed.csv")

area_policiaca = st.sidebar.selectbox("Area Policíaca", ["Todas las áreas"].extend(df["Area"].unique()))


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
  
crimenes = df["Crime"].unique().tolist()
