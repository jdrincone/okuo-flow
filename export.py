import os
import pandas as pd
import webbrowser
from datetime import datetime

def generar_reporte_okuo(
    titulo, 
    descripcion, 
    dataframe=None, 
    carpeta_imagenes=None, 
    logo_url="./images/logo_ppal.png",  # <-- Usa aquí el logo local
    nombre_archivo='reporte_okuo.html'
):
    """
    Genera un informe HTML con un diseño inspirado en la plantilla de Okuo Reporting.
    Puede incluir una tabla de datos (con scroll después de 7 filas) y gráficos.

    Parámetros:
        titulo (str): Título del informe.
        descripcion (str): Descripción del informe.
        dataframe (pd.DataFrame, opcional): DataFrame a incluir como tabla en el informe.
        carpeta_imagenes (str, opcional): Ruta de la carpeta con imágenes .png.
        logo_url (str, opcional): Ruta o URL del logo de la empresa. Por defecto busca ./images/logo_ppal.png
        nombre_archivo (str, opcional): Nombre del archivo HTML generado.
    """
    # Obtener la fecha actual
    current_date = datetime.now().strftime("%d-%m-%Y")

    # CSS y estructura inicial con scroll en la tabla
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>{titulo}</title>
        <link rel="shortcut icon" type="image/x-icon" href="images/logo.png">
        <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">
        <style>
            h3 {{
                text-align: left;
                font-family: Rubik;
                font-size: 25px;
            }}
            /* Regla específica para h3 con clase "title" */
            h3.title {{
                color: #1c8074; /* Título en color #1c8074 */
            }}

            h4 {{
                text-align: left;
                font-family: Barlow;
                /* h4.title quedará en color negro por defecto */
            }}
            h6 {{
                text-align: center;
                font-family: Helvetica;
            }}
            .title {{
                text-align: center;
                font-family: Helvetica;
            }}
            .text {{
                margin-right: 5%;
                font-size: 17px;
                font-family: Barlow;
                line-height: 1.7;
                text-align: justify
            }}
            table {{
                border: 1px solid black;
                border-collapse: collapse;
                width: 100%;
            }}
            th, td {{
                padding: 5px;
                text-align: center;
                font-family: Helvetica;
                font-size: 90%;
                border-bottom: 1px solid #ddd;
            }}
            th {{
                background-color: #f5f5f5;
                position: sticky;
                top: 0;
                z-index: 1;
            }}
            tr:hover {{
                background-color: #f1f1f1;
            }}
            .dataframe-container {{
                max-height: 300px; /* Limita la altura de la tabla para que haga scroll */
                overflow-y: auto;  /* Activa el scroll vertical */
                border: 1px solid #ddd; 
                border-radius: 8px; 
                margin: 20px auto;
            }}
            .wide {{
                width: 88%;
            }}
            .container {{
                padding-bottom:3%;
            }}
            .zoom {{
                transition: transform .2s;
                margin-left:-200px;
            }}
            .zoom:hover {{
                transform: scale(1.1);
            }}
            .footer {{
                text-align: left;
                background-color: #ffffff;
            }}
        </style>
    </head>
    <body style="margin-left:4%; margin-right:4%; margin-top:3%; margin-bottom:3%;
                padding-left:3%; padding-right:3%; padding-top:3%;
                box-shadow: 0 5px 9px 0 rgba(0, 0, 0, 0.5), 0 6px 20px 0 rgba(0, 0, 0, 0.19); border-radius:9px">
    
        <a href="https://okuo.bio/" style="float: right" target="_blank">
            <img class="zoom" width="300" src="{logo_url}" alt="Okuo Logo">
        </a>
    
        <div class="container">
            <br><br><br><br>
            <!-- h3 con clase "title": color #1c8074 -->
             <br><br>
            <h3 class="title"><strong>{titulo}</strong></h3>
            <!-- h4 con clase "title": por defecto negro -->
            <h4 class="title">Planta de producción Fazenda</h4>
            <br><br>

            <p class="text">{descripcion}</p>
            <br>
             <br><br>
            <h3 class="title"><strong>Diagramación de los datos y conteo en cada los puntos de medición</strong></h3>
             <br><br>
            
    #        <img src="images_facenda/diagrama_fazenda.svg" alt="diagrama" style="max-width:100%; display:block; margin:auto;">'
     <h3 class="title"><strong>Medida en Molienda</strong></h3>
     

        </div>
    """


    # Agregar la tabla con scroll
    if dataframe is not None:
        tabla_html = dataframe.to_html(index=False, classes='table table-striped')
        html += """
        <h4 class="title"><strong>Estadísticos descriptivos en medidas de
          Granulometría en molienda agrupados por dieta</strong></h4>
        <div class="dataframe-container">
        """
        html += tabla_html  # Se mantiene todo el DataFrame, pero con scroll
        html += "</div><br>"

    html += f""" <h4 class="title"><strong>Resumen gráfico de medidas de Granulometría de dietas con más 
    de 50 datos registrados</strong></h4>
    
      <img src="images_facenda/granulometria_violin_plots.png" alt="diagrama" style="max-width:100%; display:block; margin:auto;">'
    """
    html += f""" <p class="text">De forma genérica, el grado de la malla no discrimina por dieta, adicionalmente, 
     la malla %12 y malla %14 estan filtrando el mismo porcentaje de partículas.</p>"""

    html += "</div><br>"
    html += "</div><br>"
    # Medidas en Pellet
    html += f""" <h3 class="title"><strong>Medida en Pellet</strong></h3>
    """
    dataframe = pd.read_csv("data_facenda/estadisticos_dureza_punto_dieta.csv")
    tabla_html = dataframe.to_html(index=False, classes='table table-striped')
    html += """
        <h4 class="title"><strong>Estadísticos descriptivos en medidas de dureza por Zaranda y dieta</strong></h4>
        <div class="dataframe-container">
        """
    html += tabla_html  # Se mantiene todo el DataFrame, pero con scroll
    html += "</div><br>"
    html += f""" <p class="text">Precisaremos la anterior tabla en aquellas dietas que se realizan
      en las peletizadoras 1 y 2, con el objetivo de entender si alguna dieta posee a nivel estadístico un mejor
      resultado en medidas de dureza.</p>"""



    html += f""" <h4 class="title"><strong>Comparativa del comportamiento en la dureza del pellet de dietas
     realizadas en la peletizadora 1 y 2 </strong></h4>
    
      <img src="images_facenda/dureza_dieta_punto_violin_plots.png" alt="diagrama" style="max-width:100%; display:block; margin:auto;">'
    """
    html += f""" <p class="text">Para entender si las diferentes muestras de dietas por peletizadora
      <strong>tienden a tener valores sistemáticamente más altos o más bajos que otra en medidas de dureza</strong>, realizaremos una
    prueba de Mann-Whitney U, utilizada para comparar dos grupos independientes cuando no se puede asumir que 
    los datos siguen una distribución normal.</p>"""


    dataframe = pd.read_csv("data_facenda/prueba_mejor_dureza.csv")
    tabla_html = dataframe.to_html(index=False, classes='table table-striped')

    html += f""" <h4 class="title"><strong>Revisión con cual peletizadora y con que dieta se obtienen mejores medidas
     de dureza </strong></h4>
        """
    html += tabla_html  # Se mantiene todo el DataFrame, pero con scroll
    html += "</div><br>"
    html += f""" <h4 class="title"><strong>Comparativa entre dietas por peletizadora con diferencia significativa en la
    dureza del pellet</strong></h4>
    
      <img src="images_facenda/histograma_mejor_dieta.png" alt="diagrama" style="max-width:100%; display:block; margin:auto;">'
    """

    html += "</div><br>"
    html += "</div><br>"
    html += "</div><br>"
    html += "</div><br>"

    dataframe = pd.read_csv("data_facenda/estadisticos_porcentaje durabilidad_punto_dieta.csv")
    tabla_html = dataframe.to_html(index=False, classes='table table-striped')
    html += """
        <h4 class="title"><strong>Estadísticos descriptivos en medidas de durabilidad por Zaranda y dieta</strong></h4>
        <div class="dataframe-container">
        """
    html += tabla_html  # Se mantiene todo el DataFrame, pero con scroll
    html += "</div><br>"

    html += f""" <h4 class="title"><strong>Resumen gráfico de medidas de durabilidad para dietas realizadas
    en zarandas 1 y 2 </strong></h4>
    
      <img src="images_facenda/porcentaje durabilidad_dieta_punto_violin_plots.png" alt="diagrama" style="max-width:100%; display:block; margin:auto;">'
    """

    html += f""" <p class="text">Importante destacar que el porcentaje de durabilidad en pellet para 
    todas las dietas exceptuando C.LEVANTE P y medidas en ZARANDA 1, poseen el mismo valor central en el porcentaje
    de durabilidad, mientras que en ZARANDA 2 se observa mayor variabilidad entre distintas dietas.</p>"""

    dataframe = pd.read_csv("data_facenda/prueba_mejor_durabilidad.csv")
    tabla_html = dataframe.to_html(index=False, classes='table table-striped')
    html += """
        <h4 class="title"><strong>Revisión con cual peletizadora y con que dieta se obtienen mejores medidas
     en el porcentaje de durabilidad </strong></h4>
        <div class="dataframe-container">
        """
   
    html += tabla_html  # Se mantiene todo el DataFrame, pero con scroll
    html += "</div><br>"
    html += f""" <h4 class="title"><strong>Comparativa entre dietas por peletizadora con diferencia significativa en el porcentaje
     de durabilidad del pellet</strong></h4>
    
      <img src="images_facenda/histograma_mejor_dieta_durabilidad.png" alt="diagrama" style="max-width:100%; display:block; margin:auto;">'
    """
    


   # Medidas en Pellet
    html += f""" <h3 class="title"><strong>Medida en Temperatura</strong></h3>
    """






    # Temperatura

    dataframe = pd.read_csv("data_facenda/estadisticos_temp_punto_dieta.csv")
    tabla_html = dataframe.to_html(index=False, classes='table table-striped')
    html += "</div><br>"
    html += "</div><br>"
    html += """
        <h4 class="title"><strong>Estadísticos descriptivos en medidas de temperatura en diferentes puntos y para diferentes
        dietas</strong></h4>
        <div class="dataframe-container">
        """
    html += tabla_html  # Se mantiene todo el DataFrame, pero con scroll
    html += "</div><br>"
    html += f""" <h4 class="title"><strong>Resumen gráfico de la temperateratura por dieta en cada acondicionador. </strong></h4>
    
      <img src="images_facenda/termometro industrial_acon23_dieta_punto_violin_plots.png" alt="diagrama" style="max-width:100%; display:block; margin:auto;">'
      
    """
    #<img src="images_facenda/termometro industrial_acon12_dieta_punto_violin_plots.png" alt="diagrama" style="max-width:100%; display:block; margin:auto;">'





  
    html += f"""
        <br><br><br>
        <h6 style="font-size: 16px"> Fecha de elaboración: {current_date} </h6>
        <h6 style="font-size: 16px"><a href="https://okuo.bio/" target="_blank"> https://okuo.bio/ </a></h6>
    </body>
    <footer class="footer"></footer>
    </html>
    """

    # Guardar el contenido en un archivo HTML
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write(html)

    # Abrir automáticamente en el navegador
    webbrowser.open_new_tab(nombre_archivo)

    print(f"Informe generado: {nombre_archivo}")


# Ejemplo de uso con un DataFrame
df = pd.read_csv("data_facenda/estadisticos_granulometria_dieta.csv")

# Generar el reporte usando el logo local en 'images/logo_ppal.png'
descripcion = """
<p class="text">
    Este informe presenta un análisis estadístico detallado sobre las medidas de <strong>granulometría
    </strong> en molienda, <strong>dureza</strong> y <strong>durabilidad</strong> en pellet 
    recopiladas en <strong>Fazenda</strong>.
    Se han considerado diversos procesos de medición para proporcionar una visión integral del desempeño en la producción.
    A continuación, se detallan los aspectos analizados:
</p>

<ul class="text">
    <li>Conteo de registros en los procesos de medición.</li>
    <li>Estadísticas descriptivas para medidas en molienda tomadas en la tolva y desglosadas por cada dieta.</li>
    <li>Estimadores de tendencias centrales en granulometría para dietas con mayor cantidad de datos.</li>
    <li>Estadísticas descriptivas para dureza y durabilidad del Pellet categorizadas por:
        <strong>Dieta</strong> y <strong>Punto</strong> de toma de medidas.
    </li>
    <li>Estadísticas descriptivas en la temperatura por dieta.</li>
</ul>

<p class="text">
</p>
"""
generar_reporte_okuo(
    titulo='Análisis Estadístico sobre Granulometría en Molienda y Durabilidad en Pellet',
    descripcion=descripcion,
    dataframe=df,
    carpeta_imagenes='./images',
    logo_url='./images/logo_ppal.jpg',  # Indicamos el logo local
    nombre_archivo='reporte_okuo.html'
)
