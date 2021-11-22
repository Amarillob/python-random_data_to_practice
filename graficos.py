# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 17:51:46 2021

@author: Brian
"""
def graficar(df): 
    """
data = diccionario donde las keys son los nombres de las cripto y los 
valores asociodos son df de 2 columnas, la primera corresponde a las
fechas y la segunda a las cotizaciones

lista = debe indicar los nombres de las cripto ordenadas según el indice deseado

periodo = str que indica el nombre correspondiente a la columna de fechas

cotizacion = str que indica el nombre correspondiente a la columna de cotizaciones


    """
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_pdf import PdfPages
    import matplotlib.dates as mdates
             
    fig, ax = plt.subplots(figsize = (21,35), nrows = 10, ncols = 3)
    #agrando el espacio entre los subplots
    fig.tight_layout(pad = 5)


    aux = []
    for i in range(10):
        for _ in range(3):
            aux.append(i)
    
    aux_1 = []
    for i in range(10):
        for e in range(3):
            aux_1.append(e)
    
    aux_2 = [_ for _ in range(30)]
    
    
    
    
    criptos = list(df.columns)
    for i in range(30):
    # generalizacion de row and colum
        row = aux[i]
        colum = aux_1[i]
    
    # nombre de la cripto a graficar
        cripto_name = criptos[i]
    
    # datos a graficar
        # periodo = data[cripto_name][periodo]
        # cotizacion = data[cripto_name][cotizacion]
               
        periodo = list(df.index)
        cotizacion = list(df[cripto_name])
        
        
    
    # GRAFICO
        ax[row,colum].plot(periodo, cotizacion)
        ax[row,colum].set_title(cripto_name)
        plt.draw()  #otherwise, bug
        labels = ax[row,colum].get_xticklabels()
        ax[row,colum].set_xticklabels(labels, rotation = 45, ha = "right", size = 8)
       

    return fig