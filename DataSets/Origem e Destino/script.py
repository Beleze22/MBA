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

#%%Definindo funções úteis

def converter_to_numeric(df):
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
    return df

#%% Lendo os arquivos de 2017

Origens_por_modo_2017 = pd.read_csv("Tab16_OD2017.csv", sep=";", decimal=",")
Origens_por_tipo_2017 = pd.read_csv("Tab17_OD2017.csv", sep=";", decimal=",")
Destinos_por_modo_2017 = pd.read_csv("Tab21_OD2017.csv", sep=";", decimal=",")
Destinos_por_tipo_2017 = pd.read_csv("Tab22_OD2017.csv", sep=";", decimal=",")

Origens_por_modo_2017.info()
Origens_por_tipo_2017.info()
Destinos_por_modo_2017.info()
Destinos_por_tipo_2017.info()

#%% Lendo os arquivos de 2007

Origens_por_modo_2007 = pd.read_csv("Tab16_OD2007.csv", sep=";", decimal=",")
Origens_por_tipo_2007 = pd.read_csv("Tab17_OD2007.csv", sep=";", decimal=",")
Destinos_por_modo_2007 = pd.read_csv("Tab21_OD2007.csv", sep=";", decimal=",")
Destinos_por_tipo_2007 = pd.read_csv("Tab22_OD2007.csv", sep=";", decimal=",")

Origens_por_modo_2007.info()
Origens_por_tipo_2007.info()
Destinos_por_modo_2007.info()
Destinos_por_tipo_2007.info()


#%% Lendo e tratando os arquivos de 1997

Origens_por_modo_1997 = pd.read_csv("Tab15_OD97.csv", sep=";", decimal=",")
Origens_por_tipo_1997 = pd.read_csv("Tab16_OD97.csv", sep=";", decimal=",")
Destinos_por_modo_1997 = pd.read_csv("Tab20_OD97.csv", sep=";", decimal=",")
Destinos_por_tipo_1997 = pd.read_csv("Tab21_OD97.csv", sep=";", decimal=",")

Origens_por_modo_1997 = converter_to_numeric(Origens_por_modo_1997)

Origens_por_modo_1997.info()
Origens_por_tipo_1997.info()
Destinos_por_modo_1997.info()
Destinos_por_tipo_1997.info()

#%% Lendo e tratando os dados de 1987

Origens_por_modo_1987 = pd.read_csv("Tab9_OD87.csv", sep=";", decimal=",")
Origens_por_tipo_1987 = pd.read_csv("Tab10_OD87.csv", sep=";", decimal=",")
Destinos_por_modo_1987 = pd.read_csv("Tab13_OD87.csv", sep=";", decimal=",")
Destinos_por_tipo_1987 = pd.read_csv("Tab14_OD87.csv", sep=";", decimal=",")

Origens_por_modo_1987 = converter_to_numeric(Origens_por_modo_1987)
Origens_por_tipo_1987 = converter_to_numeric(Origens_por_tipo_1987)
Destinos_por_modo_1987 = converter_to_numeric(Destinos_por_modo_1987)
Destinos_por_tipo_1987 = converter_to_numeric(Destinos_por_tipo_1987)

Destinos_por_modo_1987.info()
Destinos_por_tipo_1987.info()
Origens_por_modo_1987.info()
Origens_por_tipo_1987.info()

#%% Lendo e tratando os dados de 1977

Origens_por_modo_1977 = pd.read_csv("Tab7_OD77.csv", sep=";", decimal=",")
Origens_por_tipo_1977 = pd.read_csv("Tab8_OD77.csv", sep=";", decimal=",")
Destinos_por_modo_1977 = pd.read_csv("Tab11_OD77.csv", sep=";", decimal=".")
Destinos_por_tipo_1977 = pd.read_csv("Tab12_OD77.csv", sep=";", decimal=",")

Destinos_por_modo_1977.info()
Destinos_por_tipo_1977.info()
Origens_por_modo_1977.info()
Origens_por_tipo_1977.info()


#%%  Resumo Zona de Origem por Tipo de Transporte
resumo_tipo = {
    'Ano': ['1977','1987', '1997', '2007', '2017'],
    'Coletivo': [Origens_por_tipo_1977['Coletivo'].sum(), Origens_por_tipo_1987['Coletivo'].sum(), 
                 Origens_por_tipo_1997['Coletivo'].sum(), Origens_por_tipo_2007['Coletivo'].sum(), 
                 Origens_por_tipo_2017['Coletivo'].sum()],
    'Individual': [Origens_por_tipo_1977['Individual'].sum(), Origens_por_tipo_1987['Individual'].sum(), 
                   Origens_por_tipo_1997['Individual'].sum(), Origens_por_tipo_2007['Individual'].sum(), 
                   Origens_por_tipo_2017['Individual'].sum()],
    }

resumo_tipo = pd.DataFrame(resumo_tipo)

#%% Resumo Zona de Origem por Modo de Transporte

Origens_por_modo_2017.columns

resumo_modo = {
    'Ano': ['1977','1987', '1997', '2007', '2017'],
    'Ônibus/Trólebus': [Origens_por_modo_1977['Ônibus'].sum(), 
                        Origens_por_modo_1987['Ônibus'].sum() + Origens_por_modo_1987['Trólebus'].sum(),
                        Origens_por_modo_1997['Ônibus'].sum(),
                        Origens_por_modo_2007['Ônibus'].sum(),
                        Origens_por_modo_2017['Ônibus'].sum()],
    'Automóvel/Táxi': [Origens_por_modo_1977['Automóvel'].sum() + Origens_por_modo_1977['Táxi'].sum(),
                  Origens_por_modo_1987['Automóvel'].sum() + Origens_por_modo_1987['Táxi'].sum(),
                  Origens_por_modo_1997['Automóvel'].sum() + Origens_por_modo_1997['Táxi'].sum(),
                  Origens_por_modo_2007['Dirigindo Automóvel'].sum() + Origens_por_modo_2007['Táxi'].sum(),
                  Origens_por_modo_2017['Automóvel'].sum() + Origens_por_modo_2017['Táxi'].sum()
                  ],
    'Moto': [Origens_por_modo_1977['Moto'].sum(), 
                        Origens_por_modo_1987['Moto'].sum(),
                        Origens_por_modo_1997['Moto'].sum(),
                        Origens_por_modo_2007['Moto'].sum(),
                        Origens_por_modo_2017['Moto'].sum()],
    'Bicicleta': [Origens_por_modo_1977['Bicicleta'].sum(), 
                        Origens_por_modo_1987['Bicicleta'].sum(),
                        Origens_por_modo_1997['Bicicleta'].sum(),
                        Origens_por_modo_2007['Bicicleta'].sum(),
                        Origens_por_modo_2017['Bicicleta'].sum()],
    'A pé': [Origens_por_modo_1977['A pé'].sum(), 
                        Origens_por_modo_1987['A pé'].sum(),
                        Origens_por_modo_1997['A pé'].sum(),
                        Origens_por_modo_2007['A pé'].sum(),
                        Origens_por_modo_2017['A pé'].sum()]
    }

resumo_modo = pd.DataFrame(resumo_modo)

inf_gerais_OD1977 = pd.read_csv("Tab1_OD77.csv", sep=";", decimal=",")

inf_gerais_OD1977.columns

Origens_por_modo_1977[['População', 'Automóveis']] = inf_gerais_OD1977[['População', 'Automóveis']]
