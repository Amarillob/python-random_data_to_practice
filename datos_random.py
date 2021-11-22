# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 13:02:24 2021

@author: Brian
"""
# generacion de datos aleatorios
import datetime
import random
import names
import pandas as pd

# names
cant_nombres = 50
names = [names.get_first_name() for _ in range(cant_nombres)]

# dates
numdays = 2000
base = datetime.datetime.today()
date_list = [base - datetime.timedelta(days = x) for x in range(numdays)]

periodos = len(date_list)


# valores
valores = []
for name in range(len(names)):
    datos = [ random.randint(1,100) for _ in range(periodos) ]
    valores.append(datos)



# dataframe
df = pd.DataFrame()
df["periodos"] = date_list
df = df.set_index("periodos")

for index, name in enumerate(names):
    df[name] = valores[index]


#elimino variables auxiliares residuales
del base, cant_nombres, date_list, datos, name, names, numdays, valores, index, periodos

