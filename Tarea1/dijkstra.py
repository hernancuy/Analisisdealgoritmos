"""
- Dijkstra
Creado por Edsger Dijkstra en 1956. Este algoritmo resuelve el problema de la ruta mas corta para una grafica con pesos no negativos en sus aristas
- Complejidad
La complejidad es de O[|V|^2+|E|]
Si se una cola de prioridad: O[|V| log|V| + |E|]
- Pseudocodigo
1. Asignar al nodo inicial una distancia tentativa de 0 y el resto el valor 'infinito'; asignar tambien predecesor nulo para todos.
2. Establecer al nodo inicial como nodo actual y crear un conjunto de nodos no visitados con todos los nodos.
3. Mientras el conjunto de nodos no visitados está vacío:
4. Para el nuevo actual u considerando sus vecinos no visitados (V) con peso W en sus aristas
    a. Si la distancia del nodo u sumada con el peso doble Bes menor a la distancia del nodo V,actualizar la distancia de v guardar a u como predecesor de v.
5. Cuando se han revisado todos los vecinos de u coma se marca como visitado y se elimina del conjunto no visitado.
6. Seleccionar el no no visitado con menor distancia tentativa y marcarlo como nuevo nodo actual. Regresar al paso 3
"""

# Clase parar definir vertice


class Vertice:
    #constructor
    def __init__(self, i):
        self.id = i
        self.visitado = False
        self.nivel = -1
        self.vecinos = []
        self.padre = None
        self.distancia = float('inf')

    def agregarVecino(self, v, p):
        if v not in self.vecinos:
            self.vecinos.append([v, p])

class Grafica:
    #constructor
    def __init__(self):
        self.vertices = {}
        
    def agregaVertice(self, v):
        if v not in self.vertices:
            self.vertices[v] = Vertice(v)

    def agregarArista(self, a, b, p):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].agregarVecino(b, p)
            self.vertices[b].agregarVecino(a, p)

    def imprimirGrafica(self):
        for v in self.vertices:
            print("La distancia del vertices "+ str(v)+ " es " +str(self.vertices[v].distancia)+ " llegando desde "+ str(self.vertices[v].padre))

    def camino(self, a, b):
        camino = [] 
        actual = b
        while actual != None:
            camino.insert(0, actual)
            actual = self.vertices[actual].padre
        return [camino, self.vertices[b].distancia]

    def minimo(self, lista):
        if len(lista) > 0:
            m = self.vertices[lista[0]].distancia
            v = lista[0]
            for e in lista:
                if m > self.vertices[e].distancia:
                    m = self.vertices[e].distancia
                    v = e
            return v

    def dijkstra(self, a):
        if a in self.vertices:
            self.vertices[a].distancia = 0
            actual = a
            noVisitados = []

            #Recorrer nodo para establecer distancia
            for v in self.vertices:
                if v != a:
                    self.vertices[v].distancia = float('inf')
                self.vertices[v].padre = None
                noVisitados.append(v)
            
            while len(noVisitados) > 0:
                for vecino in self.vertices[actual].vecinos:
                    if self.vertices[vecino[0]].visitado == False:
                        if self.vertices[actual].distancia + vecino[1] < self.vertices[vecino[0]].distancia:
                            self.vertices[vecino[0]].distancia = self.vertices[actual].distancia + vecino[1]
                            self.vertices[vecino[0]].padre = actual
                self.vertices[actual].visitado = True
                noVisitados.remove(actual)     
                

                actual = self.minimo(noVisitados)
        else:
            return False