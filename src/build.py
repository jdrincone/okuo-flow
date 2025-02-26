import os
import pandas as pd
import numpy as np


def cargar_datos(carpeta="data_raw"):
    list_dataframe = []
    for archivo in os.listdir(carpeta):
        if "pellet" in archivo.lower() and archivo.lower().endswith('.xlsx'):
            ruta_completa = os.path.join(carpeta, archivo)
            try:
                df = pd.read_excel(ruta_completa, skiprows=10)
                cond = df["Fecha Prod."].notnull()
                df = df[cond]
                list_dataframe.append(df)
            except Exception as e:
                print(f"Error leyendo {archivo}: {e}")
    dataframes = pd.concat(list_dataframe)
    return dataframes

def clear_data():
    dataframes = cargar_datos()

    dataframes["Fecha Prod."] = dataframes["Fecha Prod."].replace({"12/01/202": '2024-12-01', "10/02/202": "2024-10-02"})
    dataframes["Fecha"] = pd.to_datetime(dataframes["Fecha Prod."], errors="ignore", infer_datetime_format=True).dt.date
    dataframes = dataframes[dataframes["Punto"].notnull()]
    dataframes["Muestra"] = dataframes["Muestra"].str.strip()
    dataframes["Punto"] = dataframes["Punto"].str.strip()
    dataframes.replace({'N.A': np.nan, 'N': np.nan, 'N.A.': np.nan, "N,A": np.nan, 'N.A.': np.nan}, inplace=True)

    rename = {
        '% Durab.' : "Porcentaje Durabilidad",
        ' Dureza kg/cm²': "Dureza",
        '10,00': "Granulometría 10",
        '12,00': "Granulometría 12",
        '14,00':  "Granulometría 14", 
        '16,00':  "Granulometría 16",
        'PAN':  "Granulometría Pan",
        'ANALISTA ': "Analista"
    }
    df_filter = dataframes.rename(columns=rename)

    df_filter['Producto'] = df_filter['Producto'].str.replace(r'(?i).*FIN.*', 'FINALIZADOR', regex=True)
    df_filter['Producto'] = df_filter['Producto'].str.replace(r'(?i).*LEV.*', 'LEVANTE', regex=True)
    df_filter['Producto'] = df_filter['Producto'].str.replace(r'(?i).*ENG.*', 'ENGORDE', regex=True)
    df_filter.to_csv("../data/data.csv", index=False)


if __name__ == "__main__":
    clear_data()

