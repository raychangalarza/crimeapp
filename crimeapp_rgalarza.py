import pandas as pd
import streamlit as st
import plotly.express as px

# Title 
st.logo("crimeapp_logo.png")
st.title("Dashboard de Datos de Crímenes en Puerto Rico")

# Creating dataframe
@st.cache_data
def load_data(data):
    df = pd.read_csv(data)
    return df

df = load_data("crime_processed.csv")

