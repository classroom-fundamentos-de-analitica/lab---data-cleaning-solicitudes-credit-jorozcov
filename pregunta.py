"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():
    
    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    df = df.copy()

    #
    # Inserte su código aquí
    #

    df = df.dropna()

    df.drop("Unnamed: 0",inplace=True, axis=1)

    df.head()
    
    #correccion variable sexo
    df.sexo = df.sexo.str.lower()
    
    df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.str.lower()
    df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.str.replace('-',' ')
    df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.str.replace('_',' ')
    df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.str.strip()
    
    df.idea_negocio = df.idea_negocio.str.lower()
    df.idea_negocio = df.idea_negocio.str.replace('-',' ')
    df.idea_negocio = df.idea_negocio.str.replace('_',' ')
    df.idea_negocio = df.idea_negocio.str.strip()
    
    #correccion barrio
    df.barrio = df.barrio.str.lower()
    df.barrio = df.barrio.str.replace('-',' ')
    df.barrio = df.barrio.str.replace('_',' ')
    
    df.loc[df["fecha_de_beneficio"].str.match(r"\d{4}\/\d{2}\/\d{1,2}") , "fecha_de_beneficio"] = pd.to_datetime(
        df.loc[df["fecha_de_beneficio"].str.match(r"\d{4}\/\d{2}\/\d{1,2}") , "fecha_de_beneficio"],
        format="%Y/%m/%d"
    )

    df.loc[~df["fecha_de_beneficio"].str.match(r"\d{4}\/\d{2}\/\d{1,2}").fillna(True) , "fecha_de_beneficio"] = pd.to_datetime(
        df.loc[~df["fecha_de_beneficio"].str.match(r"\d{4}\/\d{2}\/\d{1,2}").fillna(True) , "fecha_de_beneficio"],
        format="%d/%m/%Y"
    )
    
    df["monto_del_credito"] = df["monto_del_credito"].str.replace('$', "", regex = True)
    df.monto_del_credito = df.monto_del_credito.str.strip()
    df.monto_del_credito = df.monto_del_credito.str.replace(',','', regex = True)
    df.monto_del_credito = df.monto_del_credito.astype(float)
    
    df.línea_credito = df.línea_credito.str.lower()
    df.línea_credito = df.línea_credito.str.replace('-',' ')
    df.línea_credito = df.línea_credito.str.replace('_',' ')
    df.línea_credito = df.línea_credito.str.strip()
    
    df.drop_duplicates(inplace=True)

    # df = pd.read_csv("solicitudes_credito.csv", sep=";")
    # df = df.copy()

    # #
    # # Inserte su código aquí
    # #
    
    # df = df.dropna()
    
    # df.drop("Unnamed: 0",inplace=True, axis=1)
    
    # #Limpiar monto de credito
    # df["monto_del_credito"] = df["monto_del_credito"].str.strip('$')
    # df.monto_del_credito = df.monto_del_credito.str.strip()
    # df.monto_del_credito = df.monto_del_credito.str.replace(',','')
    # df.monto_del_credito = df.monto_del_credito.str.replace('.','')
    # df.monto_del_credito = df.monto_del_credito.astype(float)
    
    # #Cambiar a variable de fecha fecha_de_beneficio
    # df.fecha_de_beneficio = pd.to_datetime(df.fecha_de_beneficio)
    # df.fecha_de_beneficio = df.fecha_de_beneficio.dt.strftime("%d-%m-%Y")
    
    # #correccion variable sexo
    # df.sexo = df.sexo.str.lower()
    
    
    # #correccion variable tipo_de_emprendimiento
    # df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.str.lower()
    # df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.str.replace('-',' ')
    # df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.str.replace('_',' ')
    # df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.str.strip()
    
    # #correccion variable idea_negocio
    # df.idea_negocio = df.idea_negocio.str.lower()
    # df.idea_negocio = df.idea_negocio.str.replace('-',' ')
    # df.idea_negocio = df.idea_negocio.str.replace('_',' ')
    # df.idea_negocio = df.idea_negocio.str.strip()
    
    # #correccion barrio
    # df.barrio = df.barrio.str.lower()
    # df.barrio = df.barrio.str.replace('-',' ')
    # df.barrio = df.barrio.str.replace('_',' ')
    
    # #correccion línea_credito

    # df.línea_credito = df.línea_credito.str.lower()
    # df.línea_credito = df.línea_credito.str.replace('-',' ')
    # df.línea_credito = df.línea_credito.str.replace('_',' ')
    # df.línea_credito = df.línea_credito.str.strip()
    
    # #df = df[(df.estrato != 0)]
    
    # df = df.drop_duplicates()
    # print(df,df.dtypes, df.monto_del_credito.values, sep='\n')
    return df
