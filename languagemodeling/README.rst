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



Cargar el corpus usando un “corpus reader” de NLTK (e.g. PlaintextCorpusReader) o definiendo uno propio.
El “corpus reader” debe proveer un método sents que permita iterar sobre las oraciones tokenizadas del corpus.
Revisar a ojo la tokenización y segmentado en oraciones. Si es muy mala, probar otras formas de tokenización/segmentado.
Modificar el script train.py para utilizar el nuevo corpus.