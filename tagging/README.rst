Procesamiento de Lenguaje Natural - UBA 2018
============================================
 
 Author: Bianchetti, Marcelo Luis
 
Trabajo Practico N 2
--------------------
 
- Ejercicio 1.
 
 Para completar la clase *POSStats* dentro del script *stats.py* fue menester generar dos estructuras de datos basadas en diccionarios de diccionarios y dos numeros enteros. En la variable de clase _tag_word_dict (del tipo defaultdict) almacené, para cada etiqueta, las palabras que la tenían junto con la cantidad de apariciones de dichas palabras (con esa etiqueta), i.e., {D: {w1: 1, w4: 1}, ..., P: {w2: 2}}; mientras que en _word_tag_dict almacené para cada palabra, sus etiquetas junto con sus apariciones, i.e., {w1: {V: 1, A: 2}, ..., wn: {N: 4}}. De este modo tengo acceso directo a todos los datos requeridos para las estadísticas, sin necesidad de mucho cálculo posterior en los getters.

 Por otro lado, al script stats le hice una pequeña modificación para que pudiera recibir el path del corpus como parámetro al ser llamado:: 
 
  stats.py [-c <corpus>]

 Y agregué un script de configuracion, denominado *configs.py*, donde almaceno los valores de los paths por default.
 
 Al intentar correr el script sobre el corpus, vi que el tipo de datos que devolvía el Reader era un *nltk.collections.LazyMap*, el cual no posee el método len(), por lo que modifiqueé el init de la clase *POSStats* para que contara las sentencias al iterar sobre el conjunto de las mismas en lugar de aplicarle len al parámetro recibido.

 Las estadísticas sobre el corpus de ancora en español fueron las siguientes.

 **+Basic Statistics**

 :Sents: 17378
 :Tokens: 517194
 :Words: 46501
 :Tags: 85
 
 =======  =========================== ===== ===== ============================
 Most Frequent POS Tags
 -----------------------------------------------------------------------------
   tag	  Description                 freq   %	   top
 =======  =========================== ===== ===== ============================
 sp000    Preposición                 79884 15.45	(de, en, a, del, con)
 nc0s000  Sustantivo Común (singular) 63452 12.27	(presidente, equipo, partido, país, año)
 da0000	  Artículo (definitivo)       54549 10.55	(la, el, los, las, El)
 aq0000   Adjetivo (descriptivo)      33906 6.56	(pasado, gran, mayor, nuevo, próximo)
 fc       Coma                        30147 5.83	(,)
 np00000  Sustantivo Propio           29111 5.63	(Gobierno, España, PP, Barcelona, Madrid)
 nc0p000  Sustantivo Común (plural)   27736 5.36	(años, millones, personas, países, días)
 fp       Punto final / aparte        17512 3.39	(.)
 rg       Adverbio (general)          15336 2.97	(más, hoy, también, ayer, ya)
 cc       Nexo Coordinante            15023 2.90	(y, pero, o, Pero, e)
 =======  =========================== ===== ===== ============================           

 =  ===== ===== ======================
 Word Ambiguity Levels
 -------------------------------------
 n  words   %	    top
 =  ===== ===== ======================
 1  43972 94.56	(, , con, por, su, El)
 2  2318  4.98	(el, en, y, ", los)
 3  180   0.39	(de, la, ., un, no)
 4  23    0.05	(que, a, dos, este, fue)
 5  5     0.01	(mismo, cinco, medio, ocho, vista)
 6  3     0.01	(una, como, uno)
 7  0     0.00	()
 8  0     0.00	()
 9  0     0.00	()
 =  ===== ===== ======================



- Ejercicio 2.
 
 Para completar la clase *BaselineTagger* dentro del script *baseline.py* utilicé una de dos estructuras de datos basadas en diccionarios desarrolladas en el ejercicio anterior, *_word_tag_dict*. Para obtener el tag mas probable para una palabra **w** entro al diccionario con esa clave y devuelvo el tag con mayor cantidad de apariciones en el conjunto de entrenamiento. Para eso ordeno el sub-diccionario de tags segun la cantidad de apariciones de mayor a menor y tomo el primer elemento. En caso de igualdad, el resultado dependerá de la implementación de la funcion **sorted()**. 

 Para poder entrenar el modelo (en realidad para poder guardar el dump del mismo) tuve que convertir los default dict a dict comunes de python, porque la funcion *pickle.dump* se quejaba del lambda. Agregué ademas al script *train.py* la posibilidad de pasarle el path del corpus como parametro, y que en el caso default lo buscara en el path almacenado en *config.py* al igual que con *stats.py*.
 Los resultados de evaluar el modelo *baseline* fueron los siguientes:

 100.0% (87.58% / 95.27% / 18.01%)

 :Accuracy: 87.58% / 95.27% / 18.01%


- Ejercicio 3.
 
 Para completar el script de features (*features.py*), utilicé principalmente funciones de strings y acceso a named-tuplas.


- Ejercicio 4.
 
 Comienzo completando la clase **MEMM** (en el script *memm.py*). En el metodo de inicializacion genero un vectorizador a partir de los features del ejercicio anterior; lo conecto mediante un pipeline con el classifier (el cual obtengo de un diccionario a partir de una clave recibida como parametro en el constructor de la clase MEMM, y calculo el conjunto de palabras conocidas a partir del conjunto de oraciones taggeadas recibido.
 Agrego el return del metodo unknown chequeando pertenencia al conjunto de palabras conocidas. Completo el metodo que etiqueta una history mirando los *n* tags previos aplicando el metodo *predict* y con eso completo el metodo para etiquetar oraciones *tag(sent)*. Para poder probar los features complejos, instancio sus clases y las agrego al vector de features. 

 Los resultados obtenidos fueron para el classifier *LogisticRegression* para n = 1, ..., 4, con dos conjuntos distintos de features::

 v1 = [word_lower,word_istitle, word_istitle, word_isupper, word_isdigit]

 v2 = v1 + [NPrevTags(2), PrevWord(word_istitle),  NextWord(word_istitle),  WordLongerThan(3)]
 
RESULTADOS:

 Tiempos de los modelos utilizando el classifier: LogisticRegression para n = 1, ..., 4

 time python scripts/train.py -m memm -c maxent -n 1 -o memm_model_maxent_1
 real	17m47.707s
 user	15m58.628s
 sys	0m7.569s

 time python scripts/train.py -m memm -c maxent -n 2 -o memm_model_maxent_2
 real	48m11.600s
 user	18m41.463s
 sys	0m8.678s

 time python scripts/train.py -m memm -c maxent -n 3 -o memm_model_maxent_3
 real	50m9.277s
 user	20m31.382s
 sys	0m9.305s
 
 time python scripts/train.py -m memm -c maxent -n 2 -o memm_model_maxent_2
 real	48m11.600s
 user	18m41.463s
 sys	0m8.678s
 



 time python scripts/eval.py -i memm_model_maxent_1 -c
 100.0% (87.67% / 0.00% / 87.67%)
 Accuracy: 87.67% / 0.00% / 87.67%

 g \ m	sp000	nc0s000	da0000	aq0000	fc	nc0p000	rg	np00000	fp	cc
 sp000	14.26	0.07	-	-	-	-	0.00	-	-	-	
 nc0s000	0.00	12.19	-	0.24	-	0.00	0.03	0.06	-	0.00	
 da0000	-	0.13	9.56	-	-	-	-	0.00	-	-	
 aq0000	0.01	2.08	-	4.89	-	0.12	0.00	0.05	-	-	
 fc	-	-	-	-	5.85	-	-	-	-	-	
 nc0p000	-	1.23	-	0.22	-	4.05	-	0.03	-	-	
 rg	0.02	0.45	-	0.05	-	-	3.11	0.03	-	0.02	
 np00000	0.00	0.36	-	-	-	-	-	3.20	-	0.00	
 fp	-	-	-	-	-	-	-	-	3.55	-	
 cc	0.00	0.01	-	-	-	-	0.05	0.00	-	3.34	

 real	1m16.078s
 user	0m59.268s
 sys	0m1.294s



 time python scripts/eval.py -i memm_model_maxent_2 -c
 100.0% (89.45% / 0.00% / 89.45%)
 Accuracy: 89.45% / 0.00% / 89.45%

 g \ m	sp000	nc0s000	da0000	aq0000	fc	nc0p000	rg	np00000	fp	cc
 sp000	14.25	0.03	-	0.05	-	0.00	0.00	-	-	-	
 nc0s000	0.00	11.80	-	0.59	-	0.01	0.01	0.06	-	0.00	
 da0000	-	0.13	9.48	0.00	-	-	-	0.00	-	-	
 aq0000	0.01	0.83	-	6.16	-	0.07	0.00	0.05	-	-	
 fc	-	-	-	-	5.85	-	-	-	-	-	
 nc0p000	-	1.27	-	0.46	-	3.68	-	0.03	-	-	
 rg	0.02	0.11	-	0.29	-	0.02	3.10	0.03	-	0.02	
 np00000	0.00	0.27	-	0.09	-	0.00	-	3.21	-	0.00	
 fp	-	-	-	-	-	-	-	-	3.55	-	
 cc	0.00	0.00	-	0.01	-	0.00	0.05	0.00	-	3.34	
 
 real	1m27.165s
 user	1m6.625s
 sys	0m1.344s




 time python scripts/eval.py -i memm_model_maxent_3 -c
 100.0% (89.37% / 0.00% / 89.37%)
 Accuracy: 89.37% / 0.00% / 89.37%

 g \ m	sp000	nc0s000	da0000	aq0000	fc	nc0p000	rg	np00000	fp	cc
 sp000	14.25	0.02	-	0.05	-	-	0.00	0.00	-	-	
 nc0s000	0.00	11.64	-	0.76	-	0.01	0.02	0.06	-	0.00	
 da0000	-	0.09	9.48	0.04	-	0.00	-	0.00	-	-	
 aq0000	0.01	0.88	-	6.09	-	0.06	0.01	0.06	-	-	
 fc	-	-	-	-	5.85	-	-	-	-	-	
 nc0p000	-	1.05	-	0.63	-	3.73	-	0.03	-	-	
 rg	0.02	0.14	-	0.27	-	0.00	3.10	0.04	-	0.02	
 np00000	0.00	0.23	-	0.11	-	0.00	-	3.21	-	0.00	
 fp	-	-	-	-	-	-	-	-	3.55	-	
 cc	0.00	0.01	-	0.01	-	0.00	0.05	0.00	-	3.34	
 
 real	1m29.595s
 user	1m7.706s
 sys	0m1.453s



 time python scripts/eval.py -i memm_model_maxent_4 -c
 100.0% (89.37% / 0.00% / 89.37%)
 Accuracy: 89.37% / 0.00% / 89.37%

 g \ m	sp000	nc0s000	da0000	aq0000	fc	nc0p000	rg	np00000	fp	cc
 sp000	14.25	0.02	-	0.05	-	-	0.00	0.00	-	-	
 nc0s000	0.00	11.64	-	0.76	-	0.01	0.02	0.06	-	0.00	
 da0000	-	0.09	9.48	0.04	-	0.00	-	0.00	-	-	
 aq0000	0.01	0.88	-	6.09	-	0.06	0.01	0.06	-	-	
 fc	-	-	-	-	5.85	-	-	-	-	-	
 nc0p000	-	1.05	-	0.63	-	3.73	-	0.03	-	-	
 rg	0.02	0.14	-	0.27	-	0.00	3.10	0.04	-	0.02	
 np00000	0.00	0.23	-	0.11	-	0.00	-	3.21	-	0.00	
 fp	-	-	-	-	-	-	-	-	3.55	-	
 cc	0.00	0.01	-	0.01	-	0.00	0.05	0.00	-	3.34	
 
 real	1m28.099s
 user	1m6.749s
 sys	0m1.551s