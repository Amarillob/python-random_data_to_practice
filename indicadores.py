# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 12:23:37 2021

@author: Brian
"""
# importo los datos
from datos_random import df


def make_indicators(df):
    
    # 
    import statistics as stc
    import operator
    
    
    # lista que contiene los nombres de las criptos
    criptos = list(df.columns)
    
    #                        volatilidad
    variance = {}
    for cripto in criptos:
        cotizaciones = list(df[cripto])
        variance_aux = stc.variance(cotizaciones)
        mean_aux = stc.mean(cotizaciones)
        ratio = variance_aux/mean_aux
    
        variance[cripto] = ratio
    
    variance_sort = sorted(variance.items(), key=operator.itemgetter(1), reverse=True)
    
    
    #                         medias
    mean = {}
    for cripto in criptos:
        cotizaciones = list(df[cripto])
        mean_aux = stc.mean(cotizaciones)
    
        mean[cripto] = mean_aux
    
    mean_sort = sorted(mean.items(), key=operator.itemgetter(1), reverse = False)
    
    
    
    #                       ratio
    ratio = {}
    for cripto in criptos:
        cotizaciones = list(df[cripto])
        cotizaciones = sorted(cotizaciones)
        max = cotizaciones[-1]
        min = cotizaciones[0]
        ratio_aux = min/max
        
        ratio[cripto] = ratio_aux
    
    ratio_sort = sorted(ratio.items(), key=operator.itemgetter(1), reverse = False)
    
    
    # creo un diccionario para ordenar los resultados
    dic = {}
    dic["variance_sort"] = variance_sort
    dic["mean_sort"] = mean_sort
    dic["ratio_sort"] = ratio_sort
    

    return dic

