Procesamiento de Lenguaje Natural - UBA 2018
============================================
 
 Author: Bianchetti, Marcelo Luis
 
Trabajo Practico N 2
--------------------
 
- Ejercicio 1.
 
 Para completar la clase POSStats dentro del script stats.py fue menester generar dos estructuras de datos basadas en diccionarios de diccionarios y dos numeros enteros. En la variable de clase _tag_word_dict almacené para cada etiqueta, las palabras que la tenian junto con la cantidad de apariciones de dichas palabras (con esa etiqueta), i.e., {D: {w1: 1, w4: 1}, ..., P: {w2: 2}}; mientras que en _word_tag_dict almacené para cada palabra, sus etiquetas junto con sus apariciones, i.e., {w1: {V: 1, A: 2}, ..., wn: {N: 4}}. De este modo tengo acceso directo a todos los datos requeridos para las estadisticas, sin necesidad de mucho calculo posterior en las funciones.

 Las estadisticas sobre el corpus de ancora en español fueron las siguientes.