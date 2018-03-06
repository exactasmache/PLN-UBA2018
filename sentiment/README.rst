Procesamiento de Lenguaje Natural - UBA 2018
============================================
 
:Author: Bianchetti, Marcelo Luis
 
Trabajo Practico N 3
--------------------
 
- Ejercicio 1.
 
 Genere un script stats que levanta de configs.py los paths para los corpus de tweets que baje de la pagina TODO. Los resultados, utilizando len de lista y la clase Counter de la libreria collections, son los siguientes:

 *GeneralTASS train tweets*

  **Total amount of tweets**: 7219
 
  :Counter: { **P+** : 1652, **NONE** : 1483, **N** : 1335, **P** : 1232, **N+** : 847, **NEU** : 670 }

 *InterTASS train tweets*

  **Total amount of tweets**: 1008
 
  :Counter: { **N** : 418, **P** : 318, **NONE** : 139, **NEU** : 133 }


- Ejercicio 2.

 Para este ejercicio modifico la clase train para que levante los paths de configs.py, al igual que para el ejercicio anterior; mejoro el script de curve.py a fin de que con los valores calculados genere graficos usando la libreria matplotlib (realizo un chequeo del sistema operativo, a fin de no necesitar instalar python como framework y poder usarlo desde el pyenv). Los graficos son almacenados en la carpeta *graphs* con extensión *.png* y con el nombre del modelo y el clasificador utilizado (en caso de corresponder). El nombre del modelo, en caso de usar *clf* lo obtengo directamente de la clase mediante el metodo **name()**. La idea de esto es poder variar el mismo segun las mejoras aplicadas a la clase. 

 Para cada variacion de modelo grafico la *accuracy*(azul) y *F1*(anaranjado) en funcion del *n*.

 **Resultados:**

 **clf sin mejoras con maxent**
 
 :Sentiment P:
  Precision: 52.89% (119/225)
  Recall: 76.28% (119/156)
  F1: 62.47%

 :Sentiment N:
  Precision: 60.65% (131/216)
  Recall: 59.82% (131/219)
  F1: 60.23%

 :Sentiment NEU:
  Precision: 15.79% (3/19)
  Recall: 4.35% (3/69)
  F1: 6.82%

 :Sentiment NONE:
  Precision: 28.26% (13/46)
  Recall: 20.97% (13/62)
  F1: 24.07%

 :Accuracy: 52.57% (266/506)
 :Macro-Precision: 39.40%
 :Macro-Recall: 40.35%
 :Macro-F1: 39.87%

 ==== === === === ====
 \    P   N   NEU NONE
 ==== === === === ====
 P    119 27  5   5
 N    60  131 7   21
 NEU  30  29  3   7
 NONE 16  29  4   13
 ==== === === === ====

 .. image:: graphs/clf_basic_maxent.png


 **clf con mejor tokenizer con maxent**

 :Sentiment P:
  Precision: 52.94% (108/204)
  Recall: 69.23% (108/156)
  F1: 60.00%
 :Sentiment N:
  Precision: 61.29% (133/217)
  Recall: 60.73% (133/219)
  F1: 61.01%
 :Sentiment NEU:
  Precision: 27.78% (5/18)
  Recall: 7.25% (5/69)
  F1: 11.49%
 :Sentiment NONE:
  Precision: 23.88% (16/67)
  Recall: 25.81% (16/62)
  F1: 24.81%
 :Accuracy: 51.78% (262/506)
 :Macro-Precision: 41.47%
 :Macro-Recall: 40.75%
 :Macro-F1: 41.11%

 ==== === === === ====
 clf con mejor tokenizer con maxent
 ---------------------
 \    P   N   NEU NONE
 ==== === === === ====
 P    108 30  5   13  
 N    54  133 6   26  
 NEU  26  26  5   12 
 NONE 16  28  2   16
 ==== === === === ====

 .. image:: graphs/clf_tkn_maxent.png

 **clf con mejor tokenizer con svm**

 :Sentiment P:
  Precision: 55.43% (102/184)
  Recall: 65.38% (102/156)
  F1: 60.00%
 :Sentiment N:
  Precision: 63.18% (127/201)
  Recall: 57.99% (127/219)
  F1: 60.48%
 :Sentiment NEU:
  Precision: 13.51% (5/37)
  Recall: 7.25% (5/69)
  F1: 9.43%
 :Sentiment NONE:
  Precision: 22.62% (19/84)
  Recall: 30.65% (19/62)
  F1: 26.03%
 :Accuracy: 50.00% (253/506)
 :Macro-Precision: 38.69%
 :Macro-Recall: 40.32%
 :Macro-F1: 39.49%

 ==== === === === ====
 clf con mejor tokenizer con svm
 ---------------------
 \    P   N   NEU NONE
 ==== === === === ====
 P    102 27  10  17  
 N    44  127 14  34  
 NEU  26  24  5   14  
 NONE 12  23  8   19 
 ==== === === === ====

 .. image:: graphs/clf_tkn_svm.png


 **clf con mejor tokenizer con mnb**

 :Sentiment P:
  Precision: 50.00% (134/268)
  Recall: 85.90% (134/156)
  F1: 63.21%
 :Sentiment N:
  Precision: 61.86% (146/236)
  Recall: 66.67% (146/219)
  F1: 64.18%
 :Sentiment NEU:
  Precision: 100.00% (0/0)
  Recall: 0.00% (0/69)
  F1: 0.00%
 :Sentiment NONE:
  Precision: 100.00% (2/2)
  Recall: 3.23% (2/62)
  F1: 6.25%
 :Accuracy: 55.73% (282/506)
 :Macro-Precision: 77.97%
 :Macro-Recall: 38.95%
 :Macro-F1: 51.95%

 ==== === === === ====
 clf con mejor tokenizer con mnb
 ---------------------
 \    P   N   NEU NONE
 ==== === === === ====
 P    134 22  0   0  
 N    73  146 0   0  
 NEU  37  32  0   0 
 NONE 24  36  0   2
 ==== === === === ====

 .. image:: graphs/clf_tkn_mnb.png



 **clf binario con maxent**

 :Sentiment P:
  Precision: 51.98% (118/227)
  Recall: 75.64% (118/156)
  F1: 61.62%
 :Sentiment N:
  Precision: 58.88% (126/214)
  Recall: 57.53% (126/219)
  F1: 58.20%
 :Sentiment NEU:
  Precision: 12.50% (2/16)
  Recall: 2.90% (2/69)
  F1: 4.71%
 :Sentiment NONE:
  Precision: 26.53% (13/49)
  Recall: 20.97% (13/62)
  F1: 23.42%
 :Accuracy: 51.19% (259/506)
 :Macro-Precision: 37.47%
 :Macro-Recall: 39.26%
 :Macro-F1: 38.35%

 ==== === === === ====
 clf binario con maxent
 ---------------------
 \    P   N   NEU NONE
 ==== === === === ====
 P    118 28  4   6
 N    65  126 6   22
 NEU  29  30  2   8
 NONE 15  30  4   13
 ==== === === === ====

 .. image:: graphs/clf_bin_maxent.png

 **clf binario con svm**

 :Sentiment P:
  Precision: 54.55% (108/198)
  Recall: 69.23% (108/156)
  F1: 61.02%
 :Sentiment N:
  Precision: 63.21% (122/193)
  Recall: 55.71% (122/219)
  F1: 59.22%
 :Sentiment NEU:
  Precision: 15.79% (6/38)
  Recall: 8.70% (6/69)
  F1: 11.21%
 :Sentiment NONE:
  Precision: 24.68% (19/77)
  Recall: 30.65% (19/62)
  F1: 27.34%
 :Accuracy: 50.40% (255/506)
 :Macro-Precision: 39.56%
 :Macro-Recall: 41.07%
 :Macro-F1: 40.30%

 ==== === === === ====
 clf binario con svm
 ---------------------
 \    P   N   NEU NONE
 ==== === === === ====
 P    108 23  10  15
 N    52  122 15  30
 NEU  29  21  6   13
 NONE 9   27  7   19
 ==== === === === ====

 .. image:: graphs/clf_bin_svm.png


 **clf binario con mnb**

 :Sentiment P:
  Precision: 48.11% (127/264)
  Recall: 81.41% (127/156)
  F1: 60.48%
 :Sentiment N:
  Precision: 59.17% (142/240)
  Recall: 64.84% (142/219)
  F1: 61.87%
 :Sentiment NEU:
  Precision: 100.00% (0/0)
  Recall: 0.00% (0/69)
  F1: 0.00%
 :Sentiment NONE:
  Precision: 50.00% (1/2)
  Recall: 1.61% (1/62)
  F1: 3.12%
 :Accuracy: 53.36% (270/506)
 :Macro-Precision: 64.32%
 :Macro-Recall: 36.97%
 :Macro-F1: 46.95%

 ==== === === === ====
 clf binario con mnb
 ---------------------
 \    P   N   NEU NONE
 ==== === === === ====
 P    127 29  0   0
 N    76  142 0   1
 NEU  37  32  0   0
 NONE 24  37  0   1
 ==== === === === ====

 .. image:: graphs/clf_bin_mnb.png


 **clf con stop_words list con maxent**

 :Sentiment P:
  Precision: 48.71% (113/232)
  Recall: 72.44% (113/156)
  F1: 58.25%
 :Sentiment N:
  Precision: 61.84% (128/207)
  Recall: 58.45% (128/219)
  F1: 60.09%
 :Sentiment NEU:
  Precision: 21.43% (3/14)
  Recall: 4.35% (3/69)
  F1: 7.23%
 :Sentiment NONE:
  Precision: 30.19% (16/53)
  Recall: 25.81% (16/62)
  F1: 27.83%
 :Accuracy: 51.38% (260/506)
 :Macro-Precision: 40.54%
 :Macro-Recall: 40.26%
 :Macro-F1: 40.40%

 ==== === === === ====
 clf con stop_words list con maxent
 ---------------------
 \    P   N   NEU NONE
 ==== === === === ====
 P    113 29  2   12
 N    66  128 6   19
 NEU  31  29  3   6
 NONE 22  21  3   16
 ==== === === === ====

 .. image:: graphs/clf_swords_maxent.png

 **clf con stop_words list con svm**

 :Sentiment P:
  Precision: 50.50% (101/200)
  Recall: 64.74% (101/156)
  F1: 56.74%
 :Sentiment N:
  Precision: 61.83% (115/186)
  Recall: 52.51% (115/219)
  F1: 56.79%
 :Sentiment NEU:
  Precision: 17.65% (6/34)
  Recall: 8.70% (6/69)
  F1: 11.65%
 :Sentiment NONE:
  Precision: 22.09% (19/86)
  Recall: 30.65% (19/62)
  F1: 25.68%
 :Accuracy: 47.63% (241/506)
 :Macro-Precision: 38.02%
 :Macro-Recall: 39.15%
 :Macro-F1: 38.57%

 ==== === === === ====
 clf con stop_words list con svm
 ---------------------
 \    P   N   NEU NONE
 ==== === === === ====
 P    101 28  6   21
 N    56  115 16  32
 NEU  26  23  6   14
 NONE 17  20  6   19
 ==== === === === ====

 .. image:: graphs/clf_swords_svm.png
 
 **clf con stop_words list con mnb**

 :Sentiment P:
  Precision: 43.88% (129/294)
  Recall: 82.69% (129/156)
  F1: 57.33%
 :Sentiment N:
  Precision: 60.71% (119/196)
  Recall: 54.34% (119/219)
  F1: 57.35%
 :Sentiment NEU:
  Precision: 20.00% (1/5)
  Recall: 1.45% (1/69)
  F1: 2.70%
 :Sentiment NONE:
  Precision: 54.55% (6/11)
  Recall: 9.68% (6/62)
  F1: 16.44%
 :Accuracy: 50.40% (255/506)
 :Macro-Precision: 44.78%
 :Macro-Recall: 37.04%
 :Macro-F1: 40.55%

 ==== === === === ====
 clf con stop_words list con mnb
 ---------------------
 \    P   N   NEU NONE
 ==== === === === ====
 P    129 24  1   2
 N    97  119 2   1
 NEU  41  25  1   2
 NONE 27  28  1   6
 ==== === === === ====

 .. image:: graphs/clf_swords_mnb.png

  
 **clf con negacion con maxent**

 :Sentiment P:
  Precision: 51.21% (106/207)
  Recall: 67.95% (106/156)
  F1: 58.40%
 :Sentiment N:
  Precision: 58.33% (140/240)
  Recall: 63.93% (140/219)
  F1: 61.00%
 :Sentiment NEU:
  Precision: 20.00% (3/15)
  Recall: 4.35% (3/69)
  F1: 7.14%
 :Sentiment NONE:
  Precision: 22.73% (10/44)
  Recall: 16.13% (10/62)
  F1: 18.87%
 :Accuracy: 51.19% (259/506)
 :Macro-Precision: 38.07%
 :Macro-Recall: 38.09%
 :Macro-F1: 38.08%

 ==== === === === ====
 clf con negacion con maxent
 ---------------------
 \    P   N   NEU NONE
 ==== === === === ====
 P    106 39  3   8
 N    55  140 6   18
 NEU  27  31  3   8
 NONE 19  30  3   10
 ==== === === === ====
  
 .. image:: graphs/clf_neg_maxent.png


 **clf con negacion con svm**

 :Sentiment P:
  Precision: 53.12% (102/192)
  Recall: 65.38% (102/156)
  F1: 58.62%
 :Sentiment N:
  Precision: 58.45% (128/219)
  Recall: 58.45% (128/219)
  F1: 58.45%
 :Sentiment NEU:
  Precision: 13.79% (4/29)
  Recall: 5.80% (4/69)
  F1: 8.16%
 :Sentiment NONE:
  Precision: 18.18% (12/66)
  Recall: 19.35% (12/62)
  F1: 18.75%
 :Accuracy: 48.62% (246/506)
 :Macro-Precision: 35.89%
 :Macro-Recall: 37.25%
 :Macro-F1: 36.55%

 ==== === === === ====
 clf con negacion con svm
 ---------------------
 \    P   N   NEU NONE
 ==== === === === ====
 P    102 37  5   12
 N    50  128 12  29
 NEU  22  30  4   13
 NONE 18  24  8   12
 ==== === === === ====

 .. image:: graphs/clf_neg_svm.png
 
 **clf con negacion con mnb**

 :Sentiment P:
  Precision: 44.93% (124/276)
  Recall: 79.49% (124/156)
  F1: 57.41%
 :Sentiment N:
  Precision: 58.85% (133/226)
  Recall: 60.73% (133/219)
  F1: 59.78%
 :Sentiment NEU:
  Precision: 100.00% (0/0)
  Recall: 0.00% (0/69)
  F1: 0.00%
 :Sentiment NONE:
  Precision: 50.00% (2/4)
  Recall: 3.23% (2/62)
  F1: 6.06%
 :Accuracy: 51.19% (259/506)
 :Macro-Precision: 63.44%
 :Macro-Recall: 35.86%
 :Macro-F1: 45.82%

 ==== === === === ====
 clf con negacion con mnb
 ---------------------
 \    P   N   NEU NONE
 ==== === === === ====
 P    124 32  0   0
 N    84  133 0   2
 NEU  39  30  0   0
 NONE 29  31  0   2
 ==== === === === ====

 .. image:: graphs/clf_neg_mnb.png



 **Features mas relevantes para cada sentimiento usando el clf con stop_words list y maxent:**
 
 Para otbener las siguientes tablas utilice la funcion *print_maxent_features* del script analysis.py, pasandole como parametro el vectorizador y el classificador modificado con lista de stop_words. Este script lo agregué al final de eval.py, mediante la opcion *--deep*, dado que ahi ya levanto el modelo entrenado y lo evaluo. 

 :N:
  =========== =========== ==========  ============  ===========
  portada     enhorabuena gracias     buena         feliz 
  -1.72087583 -1.61411829 -1.5147778  -1.41222895   -1.41042164
  peor        corrupción  recortes    muertos       triste 
  1.78473314  1.81873067  1.91682432  1.99076086    2.47628181
  =========== =========== ==========  ============  ===========
 :NEU:
  =========== =========== ==============  =========== ===========
  parados     enhorabuena puedes          tres        felicidades 
  -1.150014   -1.03717982 -0.91364664     -0.89044434 -0.86144292
  gana        decidirán   vicepresidenta  broma       expectación
  1.24276137  1.26878577  1.27755031      1.32713174  1.34644755
  =========== =========== ==============  =========== ===========
 :NONE:
  =========== =========== ==============  =========== ===========
  gracias     feliz       interesante     gran        mal 
  -1.90620348 -1.85716252 -1.82737906     -1.74255732 -1.67852606
  jugar       sesión      reunión         300         portada 
  1.20167406  1.22048877  1.26525043      1.26773251  2.42187342
  =========== =========== ==============  =========== ===========
 :P:
  =========== =========== ==============  =========== ===========
  triste      portada     urdangarin      griñan      culpa 
  -1.64422166 -1.59682204 -1.36776675     -1.35668775 -1.35352689
  genial      homenaje    gracias         felicidades enhorabuena
  1.94677427  1.99712245  2.2420285       2.32473931  2.58299915
  =========== =========== ==============  =========== ===========

 **Tweet de ejemplo, con todos los features que intervienen y sus respectivos pesos para cada clase:**

 La siguiente tabla, al igual que la anterior, se computa utilizando una funcion del script analysis.py, en este caso *print_feature_weights_for_item*, y se realiza al finalizar la ejecucion del script eval.py, si se agregó la opcion *-d* o *--deep*. Estos resultados son para el modelo que utiliza stop_words (y maxent).

 ======= =========== =========== =========== ===========
 bandera -0.25073875 -0.07730685 -0.29306683 0.50205028
 gran    -0.78957733 0.11226857  -1.74255732  1.4192134 
 hijos   -0.03697914 0.69577544  -0.06639183 -0.53354103
 ja      -0.5576505  0.08787272  -0.74400354  0.80983631
 japón   0.18120326  -0.06493422 -0.08471276 -0.0091092 
 puta    1.03660427  -0.44976595 -0.6070564  -0.5019685 
 teneis  0.03606403  0.26372942  0.04960757  -0.23969036
 ======= =========== =========== =========== ===========