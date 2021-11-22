# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 12:53:22 2021

@author: Brian
"""
import os
os.chdir(r"C:/Users/Brian/Desktop/proyectos/trading_cripto")

from datos_random import df
from indicadores import make_indicators
import pandas as pd


# %%                    desagregacion de los datos
dias = [3,7,14,60,180,720,1825]

df_desagregado = {}
for dia in dias:
    df_aux = df.iloc[0:dia]
    df_desagregado[dia] = df_aux


del df_aux,dia

#%%                         indicadores
indicadores = {}
for dia in dias:
    df = df_desagregado[dia]
    indicador = make_indicators(df)
    indicadores[dia] = indicador 
    
del dia,df, indicador    


#%%                    graficos generalizado
from graficos import graficar

# import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
# import matplotlib.dates as mdates
       


#                                 crear las carpetas
os.chdir(r"C:/Users/Brian/Desktop")
os.mkdir("graficos")
os.chdir(r"C:/Users/Brian/Desktop/graficos")
for dia in dias:
    dia = str(dia)
    os.mkdir(dia)



metodos = ["variance_sort", "mean_sort", "ratio_sort"]
for dia in dias:
    dia = str(dia)
    path = os.path.join('c:\\', 'Users', 'Brian', 'Desktop', 'graficos', dia)
    os.chdir(path)
    
    for metodo in metodos:
        os.mkdir(metodo)


# una vez creadas las carpetas, vuelvo al escritorio
os.chdir(r"C:/Users/Brian/Desktop")


#                   graficos dentro de las carpetas                                                   
for dia in dias:
    for metodo in metodos:
        dia = str(dia)
        path = os.path.join('c:\\', 'Users', 'Brian', 'Desktop', 'graficos', dia, metodo)
        os.chdir(path)
        # variables a tener en cuenta    (ambas son de los bucles)
        dia = int(dia)
        metodo = str(metodo)
        
        # obtengo las cripto que tengo que graficar segun el metodo
        criptos_graficar = []
        tuplas = indicadores[dia][metodo]
        cont = 0
        for tupla in tuplas:
            cripto = tupla[0]
            criptos_graficar.append(cripto)
            
            #como son 30 graficos, solo necesito el top 30 segun el metodo
            cont = cont + 1
            if cont == 30:
                break
                
        # creo el df a graficar
        df_graficar = pd.DataFrame()
        for cripto in criptos_graficar:
            df_graficar[cripto] = df_desagregado[dia][cripto]

             
        # grafico
        fig = graficar(df_graficar)

        # guardar grafico como PDF 
        
        pp = PdfPages("graficos.pdf")
        pp.savefig(fig)
        pp.close()

