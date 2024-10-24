import pandas as pd

def manipulate_data(data):
    df = pd.DataFrame(data)  # Convierte los datos en un DataFrame de pandas
    # Realiza las operaciones que necesites en el DataFrame
    processed_df = df.dropna()  # Por ejemplo, eliminar filas con valores nulos
    return processed_df.to_dict(orient="records")  # Devuelve el DataFrame como lista de diccionarios
