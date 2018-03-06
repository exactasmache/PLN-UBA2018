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

 **Resultados:**

 *clf sin mejoras con maxent*
 
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

 **Confusion Matrix:**

 ==== === === === ====
      P   N   NEU NONE
 ==== === === === ====
 P    119 27  5   5
 N    60  131 7   21
 NEU  30  29  3   7
 NONE 16  29  4   13
 ==== === === === ====

 .. image:: graphs/clf_basic_maxent.png