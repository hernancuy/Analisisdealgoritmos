ALG5

Entrega taller Vertex Cover.

Entrega de los integrantes:

Hernan David Cuy Salcedo
h.cuy@uniandes.edu.co
cód. 202010199
Jaime Arturo Hurtado Romero
ja.hurtado905@uniandes.edu.co
cód. 201212121



Implementación de algoritmos aproximados para problema Vertex Cover.

Para su ejecución, se requiere Python3 y el siguiente comando en una ventana de comandos:

python tarea7.py [archivo-grafo.txt] [ 1 | 2 | 3 | 4]

El archivo-grafo debe ser un archivo de texto con los ejes del grafo, a continuación el numero seleccionado para el algoritmo a ejecutar.

Los Algoritmos son :
1 Escoger arbitrariamente un eje, incluir los dos vértices conectados, descartar todos los demás ejes conectados por los vertices escogidos y repetir hasta que no queden ejes.
2 Escoger el vértice de mayor grado, descartar los ejes que llegan al vertie escogido y repetir hasta que no queden ejes.
3 Escoger arbitrariamente un eje, incluir el vértice de mayor grado de los dos vértices conectados por el eje, descartar todos los demás ejes conectados por el vértice escogido y repetir hasta que no queden ejes.
4 Escoger aleatoriamente un eje, incluir aleatoriamente uno de los dos vértices conectados, descartar todos los demás ejes conectados por el vértices escogido y repetir hasta que no queden ejes.

Al final la ejecución del algoritmo el programa mostrará, el conjunto de vertices, el tamaño del conjunto y finalmente el tiempo de ejecución en segundos.
