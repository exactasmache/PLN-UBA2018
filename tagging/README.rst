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
 sp000    14.28	0.05    -     	0       -     -       0.01  -       -     0	
 nc0s000  0.00  12.22   -       0.25    -     0.00    0.03  0.00    -     0.00 
 da0000   -     0.15    9.54    -       -     -       -     -       -     -       
 aq0000   0.01  2.05    -       4.84    -     0.13    0.00  -       -     -  
 fc       -     -       -       -       5.85  -       -     -       -     0
 nc0p000  -     1.24    -       0.20    -     4.09    -     -       -     0
 rg       0.02  0.31    -       0.04    -     -       3.27  -       -     0.02 
 np00000  0.00  2.05    -       0.00    -     0.00    -     1.52    -     0.00  
 fp       -     -       -       -       -     -       -     -       3.55  -  
 cc       0.00  0.01    -       -       -     -       0.05  0.00    -     3.34
 =======  ===== ======= ======  ======  ====  ======= ====  ======= ====  ====

0 Ejercicio 3.
 
 Para completar el script de features (*features.py*), utilicé principalmente funciones de strings y acceso a named-tuplas.


- Ejercicio 4.
 
 Comienzo completando la clase **MEMM** (en el script *memm.py*). En el metodo de inicializacion genero un vectorizador a partir de los features del ejercicio anterior; lo conecto mediante un pipeline con el classifier (el cual obtengo de un diccionario a partir de una clave recibida como parametro en el constructor de la clase MEMM, y calculo el conjunto de palabras conocidas a partir del conjunto de oraciones taggeadas recibido.
 Agrego el return del metodo unknown chequeando pertenencia al conjunto de palabras conocidas. Completo el metodo que etiqueta una history mirando los *n* tags previos aplicando el metodo *predict* y con eso completo el metodo para etiquetar oraciones *tag(sent)*. Para poder probar los features complejos, instancio sus clases y las agrego al vector de features. 

 Las pruebas fueron realizadas en una Macbook Retina con OSX El Capitan, procesador de 1.1 GHz Intel Core M con dos cores (4 virtuales) y 8 GB de memoria de 1600MHz (DDR3). Viendo que cada ejecución consumia solo un procesador, se paralelizaron no mas de 4 pruebas (en distintos procesos) a fin de no afectar mucho a los resultados.

 Se utilizaron, para los tres classifier *LogisticRegression*, *MultinomialNB* y *LinearSVC* n = 1, ..., 4, con dos conjuntos distintos de features::

  v1 = [word_lower,word_istitle, word_istitle, word_isupper, word_isdigit]

  v2 = v1 + [NPrevTags(n), PrevWord(word_istitle),  NextWord(word_istitle),  WordLongerThan(3)]

 El siguiente cuadro representa los tiempos consumidos en la generación de los modelos, su precisión sobre palabras conocidas y desconocidas y el tiempo empleado en calcular estos datos.
 
 ===========  ==  = ===== ======  ===== ======  ======  ======= ======  ===== ======
 Times and Accuracy
 -----------------------------------------------------------------------------------
 Model              Training Times              Accuracy          Accuracy Times
 ------------------ ------------------- ----------------------- --------------------
 Classifier   Fs  n real  user    sys   total   known   unknown real    user  sys     
 ===========  ==  = ===== ======  ===== ======  ======  ======= ======  ===== ======
 LRegression  v1  1 07:36 06:39   5s    87.49%  93.29%  34.93%  41s     37s   0.844s
 LRegression  v1  2 10:21 08:09   6s    87.49%  93.29%  34.93%  40s     36s   0.645s
 LRegression  v1  3 09:37 07:37   6s    -       -       -       -       -     -
 LRegression  v1  4 09:47 08:02   5s    -       -       -       -       -     -

 LRegression  v2  1 15:30 13:52   6s    87.67%  93.41%  35.79%  43s     39s   1.118s
 LRegression  v2  2 18:24 16:33   7s    89.45%  93.74%  50.69%  53s     49s   0.775s
 LRegression  v2  3 20:54 19:02   8s    89.37%  94.13%  46.30%  57s     51s   0.833s
 LRegression  v2  4 22:49 20:56   8s    89.23%  94.13%  44.87%  56s     50s   0.968s

 MultinomNB   v1  1 01:09 01:2s   1s    83.67%  90.90%  18.22%  59:26   36:49 14:07
 MultinomNB   v1  2 01:11 01:4s   1s    83.67%  90.90%  18.22%  59:29   36:56 14:00
 MultinomNB   v1  3 00:50 00:46   1s    83.67%  90.90%  18.22%  59:54   37:07 14:14
 MultinomNB   v1  4 01:05 00:59   1s  

 MultinomNB   v2  1 01:23 01:17   2s    
 MultinomNB   v2  2 01:10 01:08   1s    
 MultinomNB   v2  3 01:22 01:17   2s    
 MultinomNB   v2  4 01:20 01:17   2s

 LinearSVC    v2  1 24:35 20:39   11s   89.62%  95.32%  38.04%  01:16   01:06 1.008s
 LinearSVC    v2  2 17:49 14:18   8s    92.48%  96.91%  52.37%  00:51   00:47 0.803s
 LinearSVC    v2  3 19:08 15:28   8s    91.93%  96.82%  47.64%  01:21   01:10 1.003s
 LinearSVC    v2  4 22:32 18:41   11s   91.52%  96.60%  45.55%  01:18   01:01 1.015s
 ===========  ==  = ===== ======  ===== ======  ======  ======= ======  ===== ======

 A continuación se presentan las matrices de confusion de los dos modelos que mejores resultados dieron en cuanto a la precision (sin ser muy grande el tiempo empleado) a fin de ver mas en detalle sus errores y aciertos

 =======  ===== ======= ======  ======  ====  ======= ====  ======= ====  ====
 Matriz de confunsion del modelo que usa linear *LinearRegression* y el vector de features *v2* con n=2.
 -----------------------------------------------------------------------------
 g | m    sp000	nc0s000	da0000	aq0000	fc    nc0p000 rg    np00000 fp    cc
 =======  ===== ======= ======  ======  ====  ======= ====  ======= ====  ====
 sp000    14.25 0.03    -       0.05    -     0.00    0.00  -       -     -
 nc0s000  0.00  11.80   -       0.59    -     0.01    0.01  0.06    -     0.00 
 da0000   -     0.13    9.48    0.00    -     -       -     0.00    -     -
 aq0000   0.01  0.83    -       6.16    -     0.07    0.00  0.05    -     -
 fc       -     -       -       -       5.85  -       -     -       -     -
 nc0p000  -     1.27    -       0.46    -     3.68    -     0.03    -     -
 rg       0.02  0.11    -       0.29    -     0.02    3.10  0.03    -     0.02 
 np00000  0.00  0.27    -       0.09    -     0.00    -     3.21    -     0.00 
 fp       -     -       -       -       -     -       -     -       3.55  -
 cc       0.00  0.00    -       0.01    -     0.00    0.05  0.00    -     3.34
 =======  ===== ======= ======  ======  ====  ======= ====  ======= ====  ====

 =======  ===== ======= ======  ======  ====  ======= ====  ======= ====  ====
 Matriz de confunsion del modelo que usa linear *LinearSVC* y el vector de features *v2* con n=2.
 -----------------------------------------------------------------------------
 g | m    sp000	nc0s000	da0000	aq0000	fc    nc0p000 rg    np00000 fp    cc
 =======  ===== ======= ======  ======  ====  ======= ====  ======= ====  ====
 sp000    14.30 0.01    -       0.02    -     -       0.00  -       -     - 
 nc0s000  0.00  12.01   -       0.42    -     0.01    0.02  0.07    -     0.00  
 da0000   -     0.09    9.56    -       -     -       -     0.01    -     -  
 aq0000   0.01  0.49    -       6.55    -     0.09    0.01  0.04    -     - 
 fc       -     -       -       -       5.85  -       -     -       -     -  
 nc0p000  -     0.91    -       0.33    -     4.23    -     0.03    -     -  
 rg       0.02  0.03    -       0.22    -     0.02    3.35  0.00    -     0.02  
 np00000  0.00  0.26    -       0.07    -     0.01    -     3.23    -     0.00  
 fp       -     -       -       -       -     -       -     -       3.55  -  
 cc       0.00  -       -       0.01    -     -       0.05  0.00    -     3.34
 =======  ===== ======= ======  ======  ====  ======= ====  ======= ====  ====

 *En una primera iteracion la precisión sobre las palabras conocidas me estaba dando 0.0 para todos los modelos. Esto se debia a que el vocabulario lo calculaba a partir de la variable* **tagged_sents** *la cual era usada para generar las listas y llegaba vacia. Utilicé otra variable, una lista, generada a partir de* **tagged_sents** *y se solucionó. Pero las pruebas las tuve que rehacer todas.*


 Si estudiamos los errores de las matrices de confusion, podemos ver los errores mas comunes (y casi los unicos), estan dados por sustantivos comunes plurales etiquetados como singulares, y por sustantivos comunes singulares etiquetados como adjetivos. Un tercer error, ya menos significativo, esta dado por sustantivos propios, tagueados como comunes singulares.
 Si agregamos como features el hecho de que la palabra actual y la anterior terminen en **s**, podriamos llegar a mitigar dos de esos tres errores (singular en vez de plural o propio). Por otro lado, pareciera ser que el mejor valor para n, es 2, se me ocurre que es porque el idioma español es muy permisivo en cuanto a la ubicacion de las palabras en la oracion, lo cual hace que las sub estructuras mas comunes esten entre dos y tres palabras.