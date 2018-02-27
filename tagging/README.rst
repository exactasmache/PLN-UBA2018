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
   tag    Description                 freq   %	   top
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

 :Accuracy: 87.58% / 95.27% / 18.01%
 
 =======  ===== ======= ======  ======  ====  ======= ====  ======= ====  ====
 g | m    sp000	nc0s000	da0000	aq0000	fc    nc0p000 rg    np00000 fp    cc
 =======  ===== ======= ======  ======  ====  ======= ====  ======= ====  ====
 sp000    14.28	0.05    0     	0       0     0       0.01  0       0     0	
 nc0s000  0.00  12.22   0       0.25    0     0.00    0.03  0.00    0     0.00 
 da0000   0     0.15    9.54    0       0     0       0     0       0     0       
 aq0000   0.01  2.05    0       4.84    0     0.13    0.00  0       0     0  
 fc       0     0       0       0       5.85  0       0     0       0     0
 nc0p000  0     1.24    0       0.20    0     4.09    0     0       0     0
 rg       0.02  0.31    0       0.04    0     0       3.27  0       0     0.02 
 np00000  0.00  2.05    0       0.00    0     0.00    0     1.52    0     0.00  
 fp       0     0       0       0       0     0       0     0       3.55  0  
 cc       0.00  0.01    0       0       0     0       0.05  0.00    0     3.34
 =======  ===== ======= ======  ======  ====  ======= ====  ======= ====  ====

0 Ejercicio 3.
 
 Para completar el script de features (*features.py*), utilicé principalmente funciones de strings y acceso a named-tuplas.


- Ejercicio 4.
 
 Comienzo completando la clase **MEMM** (en el script *memm.py*). En el metodo de inicializacion genero un vectorizador a partir de los features del ejercicio anterior; lo conecto mediante un pipeline con el classifier (el cual obtengo de un diccionario a partir de una clave recibida como parametro en el constructor de la clase MEMM, y calculo el conjunto de palabras conocidas a partir del conjunto de oraciones taggeadas recibido.
 Agrego el return del metodo unknown chequeando pertenencia al conjunto de palabras conocidas. Completo el metodo que etiqueta una history mirando los *n* tags previos aplicando el metodo *predict* y con eso completo el metodo para etiquetar oraciones *tag(sent)*. Para poder probar los features complejos, instancio sus clases y las agrego al vector de features. 

 Los resultados obtenidos fueron para el classifier *LogisticRegression* para n = 1, ..., 4, con dos conjuntos distintos de features::

  v1 = [word_lower,word_istitle, word_istitle, word_isupper, word_isdigit]

  v2 = v1 + [NPrevTags(2), PrevWord(word_istitle),  NextWord(word_istitle),  WordLongerThan(3)]

 El siguiente cuadro representa los tiempos consumidos en la generación de los modelos

 ===========  ==  = ==========  ==========  ========  ======  ===== ======= ==========  ==========  ========
 Training times
 -----------------------------------------------------------------------------------------------------------
 Model                    Training Times                    Accuracy        Accuracy Times
 ------------------ --------------------------------  --------------------- --------------------------------
 Classifier   Fs  n real        user        sys       total   known unknown real        user        sys     
 ===========  ==  = ==========  ==========  ========  ======  ===== ======= ==========  ==========  ========
 LRegression  v1  1 8m29.171s   6m34.024s   0m5.690s  87.49%  0.00% 87.49%
 LRegression  v1  2 9m23.497s   7m23.294s   0m6.000s  87.49%  0.00% 87.49%
 LRegression  v1  3 9m35.827s   7m34.238s   0m6.267s  87.49%  0.00% 87.49%
 LRegression  v1  4 9m47.498s   8m2.635s    0m5.893s  87.49%  0.00% 87.49%

 LRegression  v2  1 17m47.707s  15m58.628s  0m7.569s  87.67%  0.00% 87.67%  
 LRegression  v2  2 48m11.600s  18m41.463s  0m8.678s  89.45%  0.00% 89.45%  
 LRegression  v2  3 50m9.277s   20m31.382s  0m9.305s  89.37%  0.00% 89.37%
 LRegression  v2  4 63m26.406s  20m31.344s  0m9.061s  89.37%  0.00% 89.37%

 MultinomNB   v1  1 1m9.918s    1m2.927s    0m1.467s  
 ===========  ==  = ==========  ==========  ========  ======  ===== ======= ==========  ==========  ========
