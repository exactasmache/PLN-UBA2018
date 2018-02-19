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

 A fin de que los resultados se centraran más sobre su escritura, eliminé de todos los archivos descargados, el texto de la licencia, el autor de la digitalización y cualquier otro comentario que no fuera del autor: el indice de contenidos, la tabla de definiciones, el THE END, los prólogos ajenos al autor, notas alusivas a las puestas en escena, entre otros. Dado que no eran muchos archivos, no consideré necesario hacer un parser para ello. Simplemente edité cada archivo a mano.

 Las primeras pruebas que hice utilizaron el tokenizador por default del método PlaintextCorpusReader, luego se generaron dos tokenizadores más a partir de dos expresiones regulares distintas: uno básico y otro más sofisticados (ambos se encuentran en el script utils.py). Sobre los tres tipos de tokenizadores se realizaron estadisticas simples de palabras mas utilizadas, cantidad de tokens y vocabulario. Estos resultados se encuentran en la siguientes tablas, donde las columnas de la primera denotan de izquierda a derecha: la palabra, la cantidad de apariciones utilizando el tokenizador default, el básico y el sofisticado, respectivamente.

 .. list-table: CANTIDAD DE APARICIONES
  :widths: 20 20 20 20
  :header-rows: 1

  * - palabra
    - default
    - basico
    - sofisticado
  * - the
    - 58814
    - 58800
    - 58800
  * - of 
    - 35770
    - 35744
    - 35744
  * - a 
    - 27551
    - 27547
    - 27547
  * - and 
    - 26260
    - 26232
    - 26232
  * - to 
    - 21386
    - 21241
    - 21241
  * - in 
    - 17543
    - 17511
    - 17511
  * - that 
    - 16956
    - 16956
    - 16956
  * - is 
    - 16478
    - 16478
    - 16478

 .. list-table: Vocabulario y tokens
  :widths: 20 20 20 20
  :header-rows: 1

  * - 
    - default
    - basico
    - sofisticado
  * - Vocabulario
    - 31918
    - 33887
    - 33888
  * - Tokens
    - 1161036
    - 1144844
    - 1144808

 De estos resultados se ve que, al no tener muchas abreviaciones, no hay mayor diferencia entre los tokenizadores basico y sofisticado, y, observando las oraciones tokenizadas, se ve que cualquiera de los dos funciona suficientemente bien. No se si conviene eliminar las comillas o adjuntarlas a alguna palabra o dejarlas asi.

 Un resultado interesante es que el porcentaje de palabras distintas utilizadas por Chesterton se acerca bastante al utilizado por otro autor ingles, Shakespeare: 2,96% vs 3,51%.


- Ejercicio 2.

 Para este ejercicio tuve que modificar el archivo ngram.py. En particular la clase NGram, la cual implementa la interfaz de la clase LanguageModel. 

 Primeramente debia agregar los caracteres de START = '<s>' y de END = '</s>' las oraciones y, a partir de un entero positivo n, generar una diccionario con las apariciones de los n-gramas (tambien con los n-1 gramas); para ello modifiqué el método __init__ dentro de la clase a fin de que este diccionario se creara en la instanciación. Su creacion se logra mediante dos metodos encadenados a partir de un diccionario vacio, el metodo 'get_n_grams_count_dict_by_sent' polula los ngramas con sus apariciones dada una oracion, y el método 'get_n_grams_count_dict' itera sobre la lista de oraciones, a las cuales les agrega los caracteres de inicio y de fin.

 El método count se encarga de devolver las apariciones de un n-grama dado el token. A fin de probar las funciones antedichas generé, aparte de los dos tests con n=1 y n=2 un tercer test con n=3.

 En segundo lugar completé el metodo 'cond_prob', encargado de, dado un token y el conjunto de los n-1 predecesores (siempre asumiendo que la clase se instancia con un n), devolver la probabilidad de que dicho token aparezca en una oracion. Esto se logra dividiendo la cantidad de apariciones de la oracion resultante completa (con el token) por la cantidad de apariciones de los tokens previos recibidos. 

 Luego, para completar los metodos de las probabilidades de sentencias, agregué una funcion para centralizar el cálculo tanto de la lineal como de la logaritmica; dicho método se llama 'calculate_prob' y recibe, ademas de la oracion, el tipo de probabilidad a calcular (por default es 'lineal'). Dentro del mismo se genera un conjunto de tokens previos (el cual se genera como n-1 tokens iniciales, a fin de hacer un barrido mediante una ventana) para poder reutilizar la funcion de probabilidad por token. Asimismo se completa la oracion con los tokens de principio y fin, y se itera con una ventana, realizando la suma (en caso de la logaritmica) o la multiplicacion de las probabilidades. Tuve un error cuando la probabilidad era cero para calcular el logaritmo, por lo que en dicho caso detengo la iteracion y devuelvo infinito directamente (en caso de la lineal, devuelvo 0).

 Debido a una duda que me habia surgido, en la clase Test centralicé el valor total de tokens en la variable self.total para cambiarla por 14.0 en lugar de 12.0. Si bien era un error mio creer que era 14 en lugar de 12, porque contaba el token inicial en ambas oraciones, con lo cual el total de tokens me aumentaba en dos, gracias a esa modificacion fue sencillo volverlo a 12.


- Ejercicio 3.

 Para no acceder a los metodos internos de la clase NGram, genero un getter que me devuelve los ngramas que son clave en el diccionario de _count. A esa lista le agrego la tupla vacia y la uso para generar el diccionario de probabilidades. Para ello tomo todos los ngramas de longitud n, un calculo la probabilidad de aparicion del ultimo token, dado los primeros n-1; ese valor lo guardo en el diccionario de probabilidades condicionales. En caso de n=1, todo quedará asignado a la tupla vacia.
 Para ordenar los diccionarios de menor a mayor usé la funcion 'sorted' de python al definir el diccionario por comprensión.

 El generador de tokens lo hice utilizando la funcion radom.choices, a la cual le pasé la lista de tokens junto a la lista de sus pesos. 
 Para el generador de oraciones, viendo como estaba formulado el test, forcé a que las oraciones comenzaran con el caracter de inicio a fin de generar oraciones completas. En principio gregué en el test el caracter </s> dado que lo genero, pero luego viendo como continuaba el ejercicio, vi que debía omitirlo en el generador.

 Por una cuestion de tiempo, estoy usando solamente uno de los libros de Chesterton. La idea es mas adelante usar todos.

 Unigram:

 - to . the the contain to When culture . at exhausted by and shall be not of than as inadequacy
 - Rupert t own the
 - office insincerity he
 - or , ,

 Bigram:

 - People call it , as discussed in our words as his crown the Giant-Killer really human tradition .
 - I might be even in Kensington , has always denouncing the top of foreign land . '
 - Nietzsche , her a foolish writing an ordinary things increases the diversion , They say that it ' t see Number One , but his feet .
 - Unless a diary in all round the mass of its boundaries .

 Trigram::

 - Now I found my way in which full justice is done in a corner , and the red handkerchief , I think the French Revolution , " Lie number one .
 - While they leave off talking about them , to be both happy and conscious life is sentiment than cynicism .
 - The simple result will be relieved to hear what Hook was still largely known throughout Europe , and covered every sea ; and the débris of leaves , Though Ireland be but criminal ? "
 - He could only be called reactionary .

 Quadrigram::
 
 - What did you hear ? I asked irritably .
 - Is that Wimpole ?
 - The man who would allow them to feast ?
 - A joke is by its nature more hasty than illumination art ; it is a better ale to drink , And by the time they had risen a few hundred feet higher nothing could be further from all this human experience , allied with the Christian , from their point of view , thinks long and seriously about the public needs , and he threw himself into replying to them with a sudden simplicity and cheerfulness : Oh , I knew that without seeing it , even if it should lead a man first to a negress and then to ask men to worship a being who often acted like an angry god and always like a god .


- Ejercicio 4.

 Para este ejercicio completé la clase AddOneNGram la cual hereda de NGram, por lo que tiene todos sus métodos. Para obtener la cantidad de elementos del alfabeto utilice la funcion get_ngrams de la clase NGram (generada anteriormente), haciendo un flat a la lista recibida y metiendo los elementos en un conjunto a fin de eliminar repetidos. 
 Con estos cambios generé cuatro modelos (n = 1, ..., 4)

- Ejercicio 5.

 Mediante el script eval.py analicé los 4 modelos generados en el ejercicio anterior. Los resultados son los siguientes:

 Unigram:
Log probability: -1327691.8840736155
Cross entropy: 9.555314823341218
Perplexity: 752.3785055442511

 - Log probability: -1000700.785441279
 - Cross entropy: 9.818589129026766
 - Perplexity: 903.0043510658176

 Bigram:

 - Log probability: -1467346.9789190202
 - Cross entropy: 10.560403740385038
 - Perplexity: 1510.0742159283482

 Trigram:

 - Log probability: -1792917.7352821475
 - Cross entropy: 12.903515957639891
 - Perplexity: 7662.056546441069

 Quadrigram:

 - Log probability: -1875687.7217938555
 - Cross entropy: 13.499206334699712
 - Perplexity: 11578.865905324472

- Ejercicio 6::
Para este ejercicio completé la clase InterpolatedNgrame dentro de ngram.py. Para eso primeramente actualice la funcion generate_n_grams_count_dict_by_sent dentro de la clase NGram para que admitiera un parametro extra a fin de indicarle si calcular los n y (n-1) gramas o si calcular todos los k-gramas con k=0..n. Tambien en la misma clase centralice el calculo del vocabulario en la funcion compute_vocabulary, la cual llamo desde las clases AddOneNGram e InterpolatedNgrame.

Luego completé la funcion de instanciacion de la clase, para lo cual, en primer lugar dividí el conjunto de oraciones en dos subconjuntos: de entrenamiento y de test, luego con el conjunto de entrenamiento computo el diccionario de counts y el vocabulario. A ambos los guardo en variables nombradas igual que en las clases anteriores a fin de poder usar sus metodos.

A continuacion seteo la variable de clase gamma a partir del parametro de entrada en caso de haber, sino selecciono el gamma con menor perplejidad dentro de una lista de posibles.

La funcion count() no hizo falta sobreescribirla (Al usar _count puedo usar la ya definida en la super clase NGram.

Para calcular la probabilidad condicional acepto un parametro booleano para setear si usar o no la condicion addone en el ultimo termino de la suma, y realizo la misma siguiendo la formula que figura en https://cs.famaf.unc.edu.ar/~francolq/lm-notas.pdf.

Por ultimo agregué al script train.py la opcion de linea de comandos para seleccionar la clase InterpolatedNgrame para el modelo, entrené cuatro modelos con n=1...4 sobre un conjunto de entrenamiento, y luego los evalué sobre el test obteniendo los siguientes resultados:

 Unigram:

 - Log probability: -1340283.6002042596
 - Cross entropy: 9.645936610849091
 - Perplexity: 801.1544625910676

 Bigram:

 - Log probability: -1175829.7018092459
 - Cross entropy: 8.462372267389568
 - Perplexity: 352.718214162022

 Trigram:

 - Log probability: -1168215.096599106
 - Cross entropy: 8.40757043353705
 - Perplexity: 339.57123265930886

 Quadrigram:

 - Log probability: -1167209.0829901563
 - Cross entropy: 8.400330216988774
 - Perplexity: 337.8713513351703
