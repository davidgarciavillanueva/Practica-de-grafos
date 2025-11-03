import heapq

class UnionFind:
    """Estructura para manejar conjuntos disjuntos"""
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
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
        nodo_a_indice = {nodo: i for i, nodo in enumerate(nodos)}

        # Ordenar aristas por peso
        aristas_ordenadas = sorted(grafo.obtener_aristas(), key=lambda x: x['peso'])

        uf = UnionFind(len(nodos))
        arbol_expansion = []
        costo_total = 0