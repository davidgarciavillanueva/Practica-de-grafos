
class UnionFind:
    """Estructura para manejar conjuntos disjuntos"""
    def __init__(self, n):
        self.parent = list(range(n)) # Cada nodo es su propio padre inicialmente
        self.rank = [0] * n # Rango para optimización

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) #Se va buscando recursivamente el padre
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x) # Se obtienen los padres de X y Y
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]: #Se comparaba para saber cual es mayor
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            return True
        return False
        
def kruskal(grafo):
    """Algoritmo de Kruskal para árbol de expansión mínimo"""
    # Mapear nodos a índices
    nodos = grafo.obtener_nodos()
    nodo_a_indice = {nodo: i for i, nodo in enumerate(nodos)} # Se obtienen nodos y se enumeran por indice

    # Ordenar aristas por peso
    aristas_ordenadas = sorted(grafo.obtener_aristas(), key=lambda x: x['peso']) # Se ordenan las aristas por peso

    uf = UnionFind(len(nodos)) #Se crea la instancia de UnionFind
    arbol_expansion = []
    costo_total = 0

    for arista in aristas_ordenadas:
        if len(arbol_expansion) == len(nodos) - 1: #Se revisa si hay n nodos -1 aristas
            break

        origen_idx = nodo_a_indice[arista['origen']] # Se hace etiqueta para que quede por ej: ["A":origen, "B":destino, 5]
        destino_idx = nodo_a_indice[arista['destino']]

        if uf.union(origen_idx, destino_idx):
            arbol_expansion.append(arista) #Se comprueba si se pueden unir los nodos y no forman ciclo
            costo_total += arista['peso']

    return arbol_expansion, costo_total


  
