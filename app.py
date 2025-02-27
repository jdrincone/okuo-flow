import streamlit as st
st.set_page_config(page_title="Análisis Estadístico", layout="wide")

import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import base64
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
durabilidad_pellet_path = os.path.join(base_img_path, 'durabilidad_dureza_violin_plots.png') #distrubucion_durabilidad_formula
engrase_zaranda_path = os.path.join(base_img_path, 'engrase_zaranda.png')

# Mostrar imágenes
imagen = Image.open(logo_ppal_path)
st.image(imagen, use_container_width=True)



# Imagen en el sidebar
st.sidebar.markdown(
    f"""
    <div style='text-align: center;'>
        <img src="data:image/png;base64,{base64.b64encode(open(logo_path, "rb").read()).decode()}" width="150">
    </div>
    """, 
    unsafe_allow_html=True
)

@st.cache_data
def cargar_datos(file_name):
    dataframes = pd.read_csv(f"data/{file_name}.csv")
    return dataframes


st.sidebar.markdown("""
    <h2 style='text-align: center; color: #94AF92;'>Planta de Barlovento - Aliar</h2>
""", unsafe_allow_html=True)

st.markdown("""
    <h2 style='text-align: center; color: #1f8175;'>Análisis Estadístico sobre Granulometría
  en Molienda y Durabilidad en Pellet</h2>
""", unsafe_allow_html=True)

st.markdown("""
---

Este informe presenta un análisis estadístico detallado sobre las medidas de **Granulometría en molienda** y 
**durabilidad en pellet** recopiladas en la **Planta de Barlovento** en **Aliar**.
Se han considerado diversos procesos de medición para proporcionar una visión integral del desempeño en la producción.
A continuación, se detallan los aspectos analizados:
- Conteo de Registros en los Procesos de Medición.
- Estadísticas Descriptivas para Medidas en Molienda tomadas en la tolva, desglosadas por cada dieta.
- Estimadores de Tendencias Centrales en Granulometría.
- Estadísticas Descriptivas para Dureza y Durabilidad del Pellet categorizadas por:
   **Orden de producto**, **Producto** y **Punto de medida**.
- Estadísticas Descriptivas en la temperatura por dieta.
---
""")

# df_filter = cargar_datos(file_name="data")
# st.markdown("""
#     <h3 style='text-align: center;'>Data Original </h3>
# """, unsafe_allow_html=True)
# st.dataframe(df_filter.head())

# st.markdown("""
#     <h3 style='text-align: center; margin-bottom: 0.4cm;'></h3>
# """, unsafe_allow_html=True)


st.markdown("""
    <h3 style='text-align: center;'>Diagramación de los datos y conteo en cada los puntos de medición</h3>
""", unsafe_allow_html=True)
ruta_svg = os.path.join(base_img_path, "diagrama_2.svg")
with open(ruta_svg, "r") as archivo:
    svg_contenido = archivo.read()
st.markdown(f"""<div style="text-align: center;">{svg_contenido}</div>""", unsafe_allow_html=True)

st.markdown("""
    <h3 style='text-align: center; margin-bottom: 0.4cm;'></h3>
""", unsafe_allow_html=True)

st.markdown("""
    <h2 style='text-align: center; color: #1f8175;'>Medidas en Molienda</h2>
""", unsafe_allow_html=True)

st.markdown("""
    <h3 style='text-align: center;'>Estadísticos descriptivos en medidas de Granulometría en molienda agrupados por dieta </h3>
""", unsafe_allow_html=True)

grad = cargar_datos(file_name="estadisticos_granulometria_dieta")
st.markdown("""
    <style>
    .dataframe-container {
        display: flex;
        justify-content: center;
    }
    </style>
    <div class='dataframe-container'>
    """, unsafe_allow_html=True)
st.dataframe(grad)
st.markdown("""</div>""", unsafe_allow_html=True)

st.markdown("""Los estadísticos para dietas con menos de 5 medidas carecen de interpretabilidad por falta de datos,
            por tal motivo no son presentados.  """)



st.markdown("""
    <h3 style='text-align: center; margin-bottom: 0.4cm;'></h3>
""", unsafe_allow_html=True)
st.markdown("""
    <h3 style='text-align: center;'>Estadísticos descriptivos en medidas de Granulometría en molienda
             agrupados por recategorización en la dieta </h3>
""", unsafe_allow_html=True)

grad = cargar_datos(file_name="estadisticos_granulometria_producto")
st.markdown("""
    <style>
    .dataframe-container {
        display: flex;
        justify-content: center;
    }
    </style>
    <div class='dataframe-container'>
    """, unsafe_allow_html=True)
st.dataframe(grad)
st.markdown("""</div>""", unsafe_allow_html=True)


st.markdown("""
    <h3 style='text-align: center; margin-bottom: 0.4cm;'></h3>
""", unsafe_allow_html=True)
st.markdown("""
    <h3 style='text-align: center;'>Estimadores de Tendencias Centrales en medidas de Granulometría</h3>
""", unsafe_allow_html=True)

st.markdown("""Para comparar las granulometrías de diferentes productos, se utiliza la prueba de Mann-Whitney U,
             que evalúa si existen diferencias significativas en la distribución de las granulometrías entre los grupos comparados.
            En cada etapa de medición, el p value, p ≥ 0.05 implica que:
            No hay evidencia suficiente para afirmar que las medidas en granulometrías sean diferentes entre dietas.
            En este caso, **la dieta no es un factor significativo para clasificar la granulometría en esa etapa de medición**.
            """)
st.image(violin_plots_path, caption="Gráficos de Violin de Granulometría", use_container_width=True)


st.markdown("""
    <h3 style='text-align: center; margin-bottom: 0.4cm;'></h3>
""", unsafe_allow_html=True)


st.markdown("""
    <h2 style='text-align: center; color: #1f8175;'>Medidas en Pellet</h2>
""", unsafe_allow_html=True)
st.markdown("""
    <h3 style='text-align: center;'>Estadísticos descriptivos en medidas de dureza y durabilidad en pellet por dieta</h3>
""", unsafe_allow_html=True)



grad = cargar_datos(file_name="estadisticos_durabilidad_dieta")
st.markdown("""
    <style>
    .dataframe-container {
        display: flex;
        justify-content: center;
    }
    </style>
    <div class='dataframe-container'>
    """, unsafe_allow_html=True)
st.dataframe(grad)
st.markdown("""</div>""", unsafe_allow_html=True)





#
st.markdown("""
    <h3 style='text-align: center;'>Estadísticos descriptivos en medidas de dureza y durabilidad por dieta
            y orden de producción</h3>
""", unsafe_allow_html=True)



grad = cargar_datos(file_name="estadisticos_durabilidad_dieta_op")
st.markdown("""
    <style>
    .dataframe-container {
        display: flex;
        justify-content: center;
    }
    </style>
    <div class='dataframe-container'>
    """, unsafe_allow_html=True)
st.dataframe(grad)
st.markdown("""</div>""", unsafe_allow_html=True)


st.markdown("""
    <h3 style='text-align: center; margin-bottom: 0.4cm;'></h3>
""", unsafe_allow_html=True)
st.markdown("""
    <h3 style='text-align: center;'>Estimadores de Tendencias Centrales de la dureza y durabilidad </h3>
""", unsafe_allow_html=True)
st.image(durabilidad_pellet_path, caption="Gráficos de Violin en la durabilidad del Pellet", use_container_width=True)


st.markdown("""Las colas largar observadas en las distribucciones en el porcentaje de la durabilidad se origina
            en las fechas del **13 y 14 de Dicciembre del 2024**""")

st.markdown("""
    <h3 style='text-align: center;'>¿Afecta el Pos-engrase las medidas de dureza y durabilidad en el pellet?</h3>
""", unsafe_allow_html=True)
st.image(engrase_zaranda_path, caption="Gráficos de Violin en la durabilidad del Pellet", use_container_width=True)

st.markdown("""Existe diferencia significativa a nivel estadístico que nos indica que el Pos-engrase en las
            medidas de porcentaje de durabilidad afectan el pellet, sin embargo, en medidas de dureza no se
            observa variación significativa.""")

st.markdown("""
    <h3 style='text-align: center;'>Estadísticos asociadas a la temperatura</h3>
""", unsafe_allow_html=True)

st.markdown("""
    <h4 style='text-align: center;'>Estadísticos descriptivos en medidas de temperatura en el enfriador,
             peletizadora y acondicionador</h4>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    .dataframe-container {
        display: flex;
        justify-content: center;
    }
    </style>
    <div class='dataframe-container'>
    """, unsafe_allow_html=True)
grad = cargar_datos(file_name="estadisticos_temp_punto")
st.dataframe(grad)
st.markdown("""</div>""", unsafe_allow_html=True)





st.markdown("""
    <h4 style='text-align: center;'>Estadísticos descriptivos en medidas de 
            temperatura por dieta en cada punto de medición</h4>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    .dataframe-container {
        display: flex;
        justify-content: center;
    }
    </style>
    <div class='dataframe-container'>
    """, unsafe_allow_html=True)
grad = cargar_datos(file_name="estadisticos_temp_dieta")
st.dataframe(grad)
st.markdown("""</div>""", unsafe_allow_html=True)


st.markdown("""
    <h4 style='text-align: center;'>Estadísticos descriptivos en medidas de 
            temperatura por dieta y orden de producción</h4>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    .dataframe-container {
        display: flex;
        justify-content: center;
    }
    </style>
    <div class='dataframe-container'>
    """, unsafe_allow_html=True)
grad = cargar_datos(file_name="estadisticos_temp_op")
st.dataframe(grad)
st.markdown("""</div>""", unsafe_allow_html=True)



