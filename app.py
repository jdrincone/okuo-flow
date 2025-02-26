import streamlit as st
st.set_page_config(page_title="Análisis Estadístico", layout="wide")

import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import shapiro, mannwhitneyu
from PIL import Image

# === APLICAR FUENTE BARLOW SEMIBOLD ===
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Barlow:wght@600&display=swap');
    html, body, [class*="css"]  {
        font-family: 'Barlow', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# Ruta base para las imágenes
base_img_path = "images"

# Cargar imágenes desde la carpeta data
logo_path = os.path.join(base_img_path, 'logo.png')
logo_ppal_path = os.path.join(base_img_path, 'logo_ppal.jpg')
violin_plots_path = os.path.join(base_img_path, 'granulometria_violin_plots.png')
durabilidad_pellet_path = os.path.join(base_img_path, 'durabilidad_pellet.png')
engrase_zaranda_path = os.path.join(base_img_path, 'engrase_zaranda.png')

# Mostrar imágenes
st.sidebar.image(logo_path, width=150)
imagen = Image.open(logo_ppal_path)
st.image(imagen, use_container_width=True)

@st.cache_data
def cargar_datos(carpeta="data"):
    dataframes = pd.read_csv("data/data.csv")
    return dataframes

st.markdown("""
    <h1 style='text-align: center; color: #1f8175;'>Análisis Estadístico</h1>
""", unsafe_allow_html=True)

st.markdown("""
### Informe estadístico asociado a medidas de granularidad en molienda y durabilidad en pellets:
- Conteos de registros en cada proceso de medición.
- Revisión del comportamiento de estimadores de centralidad por producto realizado.
- Verificación de pruebas de hipótesis.
""")

df_filter = cargar_datos()
st.subheader("Data Raw")
st.dataframe(df_filter.head())

ruta_svg = os.path.join(base_img_path, "data.svg")
with open(ruta_svg, "r") as archivo:
    svg_contenido = archivo.read()
st.markdown(f"""<div style="text-align: center;">{svg_contenido}</div>""", unsafe_allow_html=True)

st.markdown("""
    <h1 style='text-align: center; color: #1f8175;'>Medidas en Molienda: estadísticos asociados a la Granulometría por Producto</h1>
""", unsafe_allow_html=True)
st.image(violin_plots_path, caption="Gráficos de Violin de Granulometría", use_container_width=True)

st.markdown("""
    <h3 style='text-align: center; color: #94af92;'>¿La eficiencia del Pellet depende del producto?</h3>
""", unsafe_allow_html=True)
st.image(durabilidad_pellet_path, caption="Gráficos de Violin en la durabilidad del Pellet", use_container_width=True)

st.markdown("""
    <h3 style='text-align: center; color: #94af92;'>¿Afecta el pos engrase las medidas de dureza y durabilidad en el pellet?</h3>
""", unsafe_allow_html=True)
st.image(engrase_zaranda_path, caption="Gráficos de Violin en la durabilidad del Pellet", use_container_width=True)
