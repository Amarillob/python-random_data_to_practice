# random_data_to_practice
Debido a que pedir datos a una API es computacionalmente costoso me pareció interesante simular una base de datos de panel para poder trabajar con ella en post de preparar el programa para que reciba datos reales.

El trabajo consta de cuatro archivos:
- datos_random.py
crea un dataframe en forma de panel data, donde las filas son fechas y las columnas nombres. Los valores simulan cotizaciones de activos.
- indicadores.py
contiene una función que si se la da como input un dataframe de las características mencionadas, devuelve como output 3 indicadores sobre los valores de dichos activos en el periodo analizado. Cada indicador, a parte de tener un valor, ordena a los activos.
- graficos.py
contiene una función que tiene como input un data frame con las caracteristicas mencionadas, pero con la salvedad que el orden según filas debe ser de mayor a menor según el indicador de interés. Es decir, dado un indicador de interés se debe armar un dataframe ordenado según dicho indicador. Así, se grafica en subplots los 30 primeros activos. 
- prueba.py
parte final del trabajo. Importa y usa todos los archivos anteriores. Desagrega los datos según diferentes horizontes temporales (por ejemplo, una semana o un mes) para poder aplicar el analisis al corto plazo y al largo plazo. Luego, crea los indicadores mencionados para cada uno de estos horizontes temporales. Finalmente grafica y guarda todos estos gráficos como pdf en una carpeta en el escritorio.


Sobre esta parte final, la carpeta creada llamada "graficos" tiene subcarpetas creadas donde cada una de ellas tiene como nombre el periodo bajo análisis (por ejemplo, una carpeta se llama 7 - en referencia a que el periodo bajo análisis es de 7 días - y otra carpeta se llama 60). A su vez, cada una de estas carpetas tiene subcarpetas que representas los distintos indicadores. Dentro de cada una de estas últimas carpetas se encuentra el pdf con los 30 subplus mencionados.
