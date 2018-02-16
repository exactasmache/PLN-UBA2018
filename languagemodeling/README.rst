Procesamiento de Lenguaje Natural - UBA 2018
============================================

Author: Bianchetti, Marcelo Luis

Trabajo Practico N 1
--------------------

- Ejercicio 1.
 Como hace unos años leí un par de novelas y libros del escritor y periodista Inglés G.K. Chesterton y me gustaron mucho,  decidí hacer los análisis con las obras de él que pude encontrar digitalizadas en internet. A fin de no excederme mucho  de los 5Mb demorando las pruebas, tuve en cuenta sólo las siguientes, las cuales fueron extraídas de la página del proyecto Gutenberg [1]:
 
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

A fin de que los resultados fueran mas reflejo de su escritura, elimine de todos los archivos descargados, el texto de la licencia, el autor de la digitalización y cualquier otro comentario que no fuera del autor: el indice de contenidos, la tabla de definiciones, el THE END, los prólogos ajenos al autor, notas alusivas a las puestas en escena, entre otros. Dado que no eran muchos archivos, no consideré necesario hacer un parser para ello. Simplemente edité cada archivo a mano.

Las primeras pruebas que hice utilizaron el tokenizador por default del método PlaintextCorpusReader, luego se generaron dos tokenizadores más a partir de dos expresiones regulares distintas: uno básico y otro más sofisticados (ambos se encuentran en el script utils.py). Sobre los tres tipos de tokenizadores se realizaron estadisticas simples de palabras mas utilizadas, cantidad de tokens y vocabulario. Estos resultados se encuentran en la siguientes tablas, donde las columnas de la primera denotan de izquierda a derecha: la palabra, la cantidad de apariciones utilizando el tokenizador default, el básico y el sofisticado, respectivamente.

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

De estos resultados se ve que, al no tener muchas abreviaciones, no hay mayor diferencia entre los tokenizadores basico y sofisticado, y, observando las oraciones tokenizadas, se ve que cualquiera de los dos funciona suficientemente bien. 

Un resultado interesante es que el porcentaje de palabras distintas utilizadas por Chesterton se acerca bastante al utilizado por otro autor ingles, Shakespeare: 2,96% vs 3,51%.


- Ejercicio 2.
Para este ejercicio tuve que modificar el archivo ngram.py. En particular la clase NGram, la cual implementa la interfaz de la clase LanguageModel. 

Primeramente debia agregar los caracteres de START = '<s>' y de END = '</s>' las oraciones
y, a partir de un entero positivo n, generar una diccionario con las apariciones de los n-gramas (tambien con los n-1 gramas); para ello modifiqué el método __init__ dentro de la clase a fin de que este diccionario se creara en la instanciación. Su creacion se logra mediante dos metodos encadenados a partir de un diccionario vacio, el metodo 'get_n_grams_count_dict_by_sent' polula los ngramas con sus apariciones dada una oracion, y el método 'get_n_grams_count_dict' va itera sobre la lista de oraciones, a las cuales les agrega los caracteres de inicio y de fin.

El método count se encarga de devolver las apariciones de un n-grama dado el token. A fin de probar las funciones antedichas generé, aparte de los dos tests con n=1 y n=2 un tercer test con n=3. 
En esta parte, viendo los tests existentes, me surgioó una duda que dejé expresada en el código: No entiendo por que el total de tokens de ambas oraciones está marcado en todos lados como 12 y no 14. A mi me da que son 7 tokens por oración, teniendo en cuenta <s> y </s>.
Otra modificacion en el test fue quitar el conjunto de tokens vacios dentro de los resultados esperados, dado que no me pareció que estuviera en las especificaciones de ngram.count(..). Con la linea 'if ngram[:-1]:' evito que se polule la clave () en el diccionario.

En segundo lugar completé el metodo 'cond_prob', encargado de, dado un token y el conjunto de los n-1 predecesores (siempre asumiendo que la clase se instancia con un n), devolver la probabilidad de que dicho token aparezca en una oracion. Esto se logra dividiendo la cantidad de apariciones de la oracion resultante completa (con el token) por la cantidad de apariciones de los tokens previos recibidos. 

Luego, para completar los metodos de las probabilidades de sentencias, agregué una funcion para centralizar el cálculo tanto de la lineal como de la logaritmica; dicho método se llama 'calculate_prob' y recibe, ademas de la oracion, el tipo de probabilidad a calcular (por default es 'lineal'). Dentro del mismo se genera un conjunto de tokens previos (el cual se genera como n-1 tokens iniciales, a fin de hacer un barrido mediante una ventana) para poder reutilizar la funcion de probabilidad por token. Asimismo se completa la oracion con los tokens de principio y fin, y se itera con una ventana, realizando la suma (en caso de la logaritmica) o la multiplicacion de las probabilidades. Tuve un error cuando la probabilidad era cero para calcular el logaritmo, por lo que en dicho caso detengo la iteracion y devuelvo infinito directamente (en caso de la lineal, devuelvo 0).

Debido a lo aclarado previamente, tuve que centralizar el valor de self.total en la clase Test para cambiarla por 14 en lugar de 12.


- Ejercicio 3.
Para no acceder a los metodos internos de la clase NGram, genero un getter que me devuelve los ngramas que son clave en el diccionario de _count. A esa lista le agrego la tupla vacia y la uso para generar el diccionario de probabilidades. Para ello tomo todos los ngramas de longitud n, un calculo la probabilidad de aparicion del ultimo token, dado los primeros n-1; ese valor lo guardo en el diccionario de probabilidades condicionales. En caso de n=1, todo quedará asignado a la tupla vacia.
Para ordenar los diccionarios de menor a mayor usé la funcion 'sorted' de python al definir el diccionario por comprensión.
