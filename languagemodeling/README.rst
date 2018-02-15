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

Las primeras pruebas que hice utilizaron el tokenizador por default del método PlaintextCorpusReader, dando como resultado
que las 10 palabras mas frecuentes eran:
the: 58814 veces,
, : 51626 veces
. : 43909 veces
of : 35770 veces
a : 27551 veces
and : 26260 veces
to : 21386 veces
in : 17543 veces
that : 16956 veces
is : 16478 veces

Con un vocabulario de 31918 palabras en un total de 1161036 tokens.

Mientras que aplicnado una expresion regular (que se encuentra en el script train.py) los resultados variaron levemente 
disminuyendo en primer lugar la cantidad tokens y el vocabulario, 1144844 y 33887 respectivamente; mientras que las 10 
palabras mas frecuentes siguieron siendo las mismas pero la cantidad de apariciones de algunas disminuyó:

the : 58800 veces
, : 55584 veces
. : 47348 veces
of : 35744 veces
a : 27547 veces
and : 26232 veces
to : 21241 veces
in : 17511 veces
that : 16956 veces
is : 16478 veces


- Ejercicio 2.
