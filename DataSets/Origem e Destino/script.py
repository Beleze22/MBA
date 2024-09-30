# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%% Instalação de Pacotes

!pip install pandas
!pip install numpy
!pip install matplotlib
!pip install seaborn
!pip install plotly
!pip install xlrd

#%% Importação de Pacotes

import pandas as pd
import numpy as np

#%% Lendo e tratando os arquivos de 2007

Origens_por_modo_2007 = pd.read_excel("Tab16_OD2007.xlsx")
Origens_por_tipo_2007 = pd.read_excel("Tab17_OD2007.xlsx")
Destinos_por_modo_2007 = pd.read_excel("Tab21_OD2007.xlsx")
Destinos_por_tipo_2007 = pd.read_excel("Tab22_OD2007.xlsx")

def converter_to_numeric(df):
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    return df

def processar_dataFrame2007(df):
    df = df.iloc[:468]
    df = df.drop(df.index[0:6])
    df = df.reset_index(drop=True)
    df = df.drop(df.index[1])
    df = df.reset_index(drop=True)
    df.columns = df.iloc[0]
    df = df.drop(df.index[0])
    return df



Origens_por_modo_2007 = processar_dataFrame2007(Origens_por_modo_2007)
Origens_por_tipo_2007 = processar_dataFrame2007(Origens_por_tipo_2007)
Destinos_por_modo_2007 = processar_dataFrame2007(Destinos_por_modo_2007)
Destinos_por_tipo_2007 = processar_dataFrame2007(Destinos_por_tipo_2007)

colunas2007 = list(Destinos_por_tipo_2007.columns)
colunas2007[0] = "Zona"
colunas2007[5] = "Total"
Destinos_por_tipo_2007.columns = colunas2007

Origens_por_modo_2007 = converter_to_numeric(Origens_por_modo_2007)
Origens_por_tipo_2007 = converter_to_numeric(Origens_por_tipo_2007)
Destinos_por_modo_2007 = converter_to_numeric(Destinos_por_modo_2007)
Destinos_por_tipo_2007 = converter_to_numeric(Destinos_por_tipo_2007)


#%% Lendo e tratando os arquivos de 1997

Origens_por_modo_1997 = pd.read_excel("Tab15_OD97.xls")
Origens_por_tipo_1997 = pd.read_excel("Tab16_OD97.xls")
Destinos_por_modo_1997 = pd.read_excel("Tab20_OD97.xls")
Destinos_por_tipo_1997 = pd.read_excel("Tab21_OD97.xls")

def processar_dataFrame1997(df):
    df = df.iloc[:369]
    df = df.drop(df.index[0:6])
    df = df.reset_index(drop=True)
    df.columns = df.iloc[0]
    df = df.drop(df.index[0])
    return df

Origens_por_modo_1997 = processar_dataFrame1997(Origens_por_modo_1997)
Origens_por_tipo_1997 = processar_dataFrame1997(Origens_por_tipo_1997)
Destinos_por_modo_1997 = processar_dataFrame1997(Destinos_por_modo_1997)
Destinos_por_tipo_1997 = processar_dataFrame1997(Destinos_por_tipo_1997)

colunas1997 = list(Destinos_por_modo_1997.columns)
colunas1997[4] = "Automóvel"
colunas1997[5] = "Automóvel.2"
Destinos_por_modo_1997.columns = colunas1997
Destinos_por_modo_1997["Automóvel"] = Destinos_por_modo_1997["Automóvel"] + Destinos_por_modo_1997["Automóvel.2"]
Destinos_por_modo_1997 = Destinos_por_modo_1997.drop(columns=["Automóvel.2"])

Origens_por_modo_1997 = converter_to_numeric(Origens_por_modo_1997)
Origens_por_tipo_1997 = converter_to_numeric(Origens_por_tipo_1997)
Destinos_por_modo_1997 = converter_to_numeric(Destinos_por_modo_1997)
Destinos_por_tipo_1997 = converter_to_numeric(Destinos_por_tipo_1997)
