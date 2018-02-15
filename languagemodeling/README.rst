Procesamiento de Lenguaje Natural - UBA 2018
============================================

Author: Bianchetti, Marcelo Luis

Trabajo Practico N 1
--------------------

- Ejercicio 1.
 Como hace unos años leí un par de novelas y libros del escritor y periodista Inglés G.K. Chesterton y me gustaron mucho, 
 decidí hacer los análisis con las obras de él que pude encontrar digitalizadas en internet. A fin de no excederme mucho 
 de los 5Mb demorando las pruebas, tuve en cuenta sólo las siguientes, las cuales fueron extraídas de la página del 
 proyecto Gutenberg [1]:
 
  - A Short History of England
  - Magic
  - The Defendant
  - Tremendous Trifles
  - All Things Considered
  - Manalive
  - The Man Who Knew Too Much
  - Utopia of Usurers and other Essays
  - Ballad of the White Horse
  - Orthodoxy
  - The Napoleon of Notting Hill
  - What I Saw in America
  - Eugenics and Other Evils
  - The Ball and The Cross
  - The Victorian Age in Literature
  - Whats Wrong in the World
  - Heretics
  - The Club of Queer Trades
  - The Wisdom of Father Brown

A fin de que los resultados fueran mas reflejo de su escritura, elimine de todos los archivos descargados, el texto de la 
licencia, el autor de la digitalización y cualquier otro comentario que no fuera del autor: el indice de contenidos, la 
tabla de definiciones, el THE END, los prólogos ajenos al autor, notas alusivas a las puestas en escena, entre otros.
Dado que no eran muchos archivos, no consideré necesario hacer un parser para ello. Simplemente edité cada archivo a mano.

Las primeras pruebas que hice utilizaron el tokenizador por default del método PlaintextCorpusReader, luego se generaron 
dos tokenizadores más a partir de dos expresiones regulares distintas: uno básico y otro más sofisticados (ambos se encuentran
en el script utils.py). Sobre los tres tipos de tokenizadores se realizaron estadisticas simples de palabras mas utilizadas,
cantidad de tokens y vocabulario. Estos resultados se encuentran en la siguientes tablas, donde las columnas de la primera denotan
de izquierda a derecha: la palabra, la cantidad de apariciones utilizando el tokenizador default, el básico y el sofisticado, respectivamente.

CANTIDAD DE APARICIONES
palabra   default   basico    sofisticado
the     : 58814     58800     58800
,       : 51626     55584     55584
.       : 43909     47348     47312
of      : 35770     35744     35744
a       : 27551     27547     27547
and     : 26260     26232     26232
to      : 21386     21241     21241
in      : 17543     17511     17511
that    : 16956     16956     16956
is      : 16478     16478     16478

              default   basico    sofisticado
Vocabulario : 31918     33887     33888
Tokens      : 1161036   1144844   1144808

De estos resultados se ve que, al no tener muchas abreviaciones, no hay mayor diferencia entre los tokenizadores basico 
y sofisticado, y, observando las oraciones tokenizadas, se ve que cualquiera de los dos funciona suficientemente bien. 
Un resultado interesante es que el porcentaje de palabras distintas utilizadas por Chesterton se acerca bastante al 
utilizado por otro autor ingles, Shakespeare: 2,96% vs 3,51%.


- Ejercicio 2.
