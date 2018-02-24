Procesamiento de Lenguaje Natural - UBA 2018
============================================
 
 Author: Bianchetti, Marcelo Luis
 
Trabajo Practico N 2
--------------------
 
- Ejercicio 1.
 
 Para completar la clase POSStats dentro del script stats.py fue menester generar dos estructuras de datos basadas en diccionarios de diccionarios y dos numeros enteros. En la variable de clase _tag_word_dict almacené para cada etiqueta, las palabras que la tenian junto con la cantidad de apariciones de dichas palabras (con esa etiqueta), i.e., {D: {w1: 1, w4: 1}, ..., P: {w2: 2}}; mientras que en _word_tag_dict almacené para cada palabra, sus etiquetas junto con sus apariciones, i.e., {w1: {V: 1, A: 2}, ..., wn: {N: 4}}. De este modo tengo acceso directo a todos los datos requeridos para las estadisticas, sin necesidad de mucho calculo posterior en las funciones.

 Por otro lado, al script stats le hice una pequeña modificación para que pudiera recibir el path del corpus como parametro al ser llamado:: 
 
 stats.py [-c <corpus>]

 Y agregué un script de configuracion, denominado configs.py, donde almaceno los valores de los paths por default.
 
 Al intentar correr el script sobre el corpus, vi que el tipo de datos que devolvia el Reader era un nltk.collections.LazyMap, el cual no posee el método len(), por lo que modifiqueé el init de la clase POSStats para que contara las sentencias al iterar sobre el conjunto de las mismas en lugar de aplicarle len al parametro recibido.

 Las estadisticas sobre el corpus de ancora en español fueron las siguientes.

 Using the default corpus ancora-3.0.1es
 =======================================
 
 Basic Statistics
 ================
 sents: 17378
 tokens: 517194
 words: 46501
 tags: 85
 
 Most Frequent POS Tags
 ======================
 tag	freq	%	top
 sp000	79884	15.45	(de, en, a, del, con)
 nc0s000	63452	12.27	(presidente, equipo, partido, país, año)
 da0000	54549	10.55	(la, el, los, las, El)
 aq0000	33906	6.56	(pasado, gran, mayor, nuevo, próximo)
 fc	30147	5.83	(,)
 np00000	29111	5.63	(Gobierno, España, PP, Barcelona, Madrid)
 nc0p000	27736	5.36	(años, millones, personas, países, días)
 fp	17512	3.39	(.)
 rg	15336	2.97	(más, hoy, también, ayer, ya)
 cc	15023	2.90	(y, pero, o, Pero, e)
 
 Word Ambiguity Levels
 =====================
 n	words	%	top
 1	43972	94.56	(,, con, por, su, El)
 2	2318	4.98	(el, en, y, ", los)
 3	180	0.39	(de, la, ., un, no)
 4	23	0.05	(que, a, dos, este, fue)
 5	5	0.01	(mismo, cinco, medio, ocho, vista)
 6	3	0.01	(una, como, uno)
 7	0	0.00	()
 8	0	0.00	()
 9	0	0.00	()

