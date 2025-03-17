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
base_img_path = "images_facenda"

# Cargar imágenes desde la carpeta data
logo_path = os.path.join("images", 'logo.png')
logo_ppal_path = os.path.join("images", 'logo_ppal.jpg')
violin_plots_path = os.path.join(base_img_path, 'granulometria_violin_plots.png')
dureza_dieta_punto_violin_plots_path = os.path.join(base_img_path, 'dureza_dieta_punto_violin_plots.png')
durabilidad_dieta_punto_violin_plots_path = os.path.join(base_img_path, 'porcentaje durabilidad_dieta_punto_violin_plots.png')


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
def cargar_datos(file_name, root="data_facenda"):
    dataframes = pd.read_csv(f"{root}/{file_name}.csv")
    return dataframes


st.sidebar.markdown("""
    <h2 style='text-align: center; color: #94AF92;'>Finca la Fazenda</h2>
""", unsafe_allow_html=True)

st.markdown("""
    <h2 style='text-align: center; color: #1f8175;'>Análisis Estadístico sobre 
            Granulometría en Molienda y Durabilidad en Pellet</h2>
""", unsafe_allow_html=True)

st.markdown("""
---
Este informe presenta un análisis estadístico detallado sobre las medidas de granulometría en molienda,
 dureza y durabilidad en pellet recopiladas en la **Fazenda**.
 Se han considerado diversos procesos de medición para proporcionar una visión integral del 
desempeño en la producción. 
A continuación, se detallan los aspectos analizados:

- Conteo de registros en los procesos de medición.
- Estadísticas descriptivas para medidas en molienda tomadas en la tolva y desglosadas por cada dieta.
- Estimadores de tendencias centrales en granulometría para dietas con mayor cantidad de datos.
- Estadísticas descriptivas para dureza y durabilidad del Pellet categorizadas por: Dieta y Punto de toma de medidas.
- Estadísticas descriptivas en la temperatura por dieta.

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
ruta_svg = os.path.join("images_facenda", "diagrama_fazenda.svg")
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
st.markdown("""
De forma genérica, el grado de la malla no discrimina por dieta, adicionalmente, 
            la malla %12 y malla %14 estan filtrando el mismo porcentaje de partículas.

""")




# st.markdown("""
#     <h3 style='text-align: center; margin-bottom: 0.4cm;'></h3>
# """, unsafe_allow_html=True)
# st.markdown("""
#     <h3 style='text-align: center;'>Estadísticos descriptivos en medidas de Granulometría en molienda
#              agrupados por recategorización en la dieta </h3>
# """, unsafe_allow_html=True)

# grad = cargar_datos(file_name="estadisticos_granulometria_producto")
# st.markdown("""
#     <style>
#     .dataframe-container {
#         display: flex;
#         justify-content: center;
#     }
#     </style>
#     <div class='dataframe-container'>
#     """, unsafe_allow_html=True)
# st.dataframe(grad)
# st.markdown("""</div>""", unsafe_allow_html=True)


st.markdown("""
    <h3 style='text-align: center; margin-bottom: 0.2cm;'></h3>
""", unsafe_allow_html=True)
st.markdown("""
    <h3 style='text-align: center;'>Resumen gráfico de medidas de Granulometría</h3>
""", unsafe_allow_html=True)

# st.markdown("""Para comparar las granulometrías de diferentes productos, se utiliza la prueba de Mann-Whitney U,
#              que evalúa si existen diferencias significativas en la distribución de las granulometrías entre los grupos comparados.
#             En cada etapa de medición, el p value, p ≥ 0.05 implica que:
#             No hay evidencia suficiente para afirmar que las medidas en granulometrías sean diferentes entre dietas.
#             En este caso, **la dieta no es un factor significativo para clasificar la granulometría en esa etapa de medición**.
#             """)
st.image(violin_plots_path, caption="Gráficos de Violin de Granulometría", use_container_width=True)


st.markdown("""
    <h3 style='text-align: center; margin-bottom: 0.4cm;'></h3>
""", unsafe_allow_html=True)


st.markdown("""
    <h2 style='text-align: center; color: #1f8175;'>Medición en Pellet</h2>
""", unsafe_allow_html=True)
st.markdown("""
    <h3 style='text-align: center;'>Estadísticos descriptivos en medidas de dureza por Zaranda y dieta
</h3>
""", unsafe_allow_html=True)

grad = cargar_datos(file_name="estadisticos_dureza_punto_dieta")
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


st.markdown("""Precisaremos la anterior tabla en aquellas dietas que se realizan en las peletizadoras 1 y 2,
             con el objetivo de entender si alguna dieta posee a nivel estadístico un mejor
             resultado en medidas de dureza:""")

st.image(dureza_dieta_punto_violin_plots_path, caption="Gráficos de Violin de Dureza por dieta y punto de medida", use_container_width=True)

st.markdown("""'
Para entender si las diferentes muestras de dietas por peletizadora **tienden a tener valores sistemáticamente 
            más altos o más bajos que otra en medidas de dureza**, 
            realizaremos una prueba de Mann-Whitney U,
             utilizada para comparar dos grupos independientes cuando no se puede asumir
             que los datos siguen una distribución normal"""
            
            )


grad = cargar_datos(file_name="prueba_mejor_dureza")
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
    <h3 style='text-align: center;'>Comparativa entre dietas por peletizadora con diferencia significativa en 
            la dureza del pellet
</h3>
""", unsafe_allow_html=True)

hist_dureza = os.path.join(base_img_path, 'histograma_mejor_dieta.png')

st.image(hist_dureza, caption="", use_container_width=True)



st.markdown("""
    <h3 style='text-align: center;'>Estadísticos descriptivos en medidas de durabilidad por Zaranda y dieta</h3>
""", unsafe_allow_html=True)



grad = cargar_datos(file_name="estadisticos_porc_durabilidad_punto_dieta")
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



st.image(durabilidad_dieta_punto_violin_plots_path, caption="Gráficos de Violin de Durabilidad por dieta y punto de medida", use_container_width=True)
st.markdown("""Importante destacar que el porcentaje de durabilidad en pellet para todas las dietas
             exceptuando C.LEVANTE P y medidas en ZARANDA 1, poseen el mismo valor central 
            en el porcentaje de durabilidad, mientras que en ZARANDA 2 se observa mayor
             variabilidad entre distintas dietas.""")

st.markdown("""
    <h3 style='text-align: center;'>Revisión con cual peletizadora y con que dieta se obtienen mejores
             medidas en el porcentaje de durabilidad</h3>
""", unsafe_allow_html=True)

grad = cargar_datos(file_name="prueba_mejor_durabilidad")
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
    <h3 style='text-align: center;'>Comparativa entre dietas por peletizadora con
             diferencia significativa en la durabilidad del pellet
</h3>
""", unsafe_allow_html=True)

hist_dureza = os.path.join(base_img_path, 'histograma_mejor_dieta_durabilidad.png')

st.image(hist_dureza, caption="", use_container_width=True)


st.markdown("""
    <h2 style='text-align: center; color: #1f8175;'>Medidas en Temperatura</h2>
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
    <h4 style='text-align: center;'>Diferencias representativas en la temperateratura por dieta en cada acondicionador.
</h4>
""", unsafe_allow_html=True)
hist_dureza = os.path.join(base_img_path, 'termometro industrial_acon12_dieta_punto_violin_plots.png')

st.image(hist_dureza, caption="", use_container_width=True)

hist_dureza = os.path.join(base_img_path, 'termometro industrial_acon23_dieta_punto_violin_plots.png')

st.image(hist_dureza, caption="", use_container_width=True)
