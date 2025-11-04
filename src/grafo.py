class GraphList:
    def __init__(self, dirigido=False):
        self.adj_list = {}
        self.pesos = {}
        self.size = 0
        self.dirigido = dirigido

    def agregar_nodo(self, value):
        if value in self.adj_list:
            return None
        self.adj_list[value] = []
        self.size += 1

    def agregar_arista(self, vertex_1, vertex_2, distancia, costo_combustible):
        if vertex_1 not in self.adj_list:
            self.agregar_nodo(vertex_1)
        if vertex_2 not in self.adj_list:
            self.agregar_nodo(vertex_2)

        peso = (distancia / 10) * costo_combustible
        
        if vertex_2 not in self.adj_list[vertex_1]:
            self.adj_list[vertex_1].append(vertex_2)
            self.pesos[(vertex_1, vertex_2)] = peso

        if not self.dirigido and vertex_1 not in self.adj_list[vertex_2]:
            self.adj_list[vertex_2].append(vertex_1)
            self.pesos[(vertex_2, vertex_1)] = peso

    def obtener_vecinos(self, vertex):
        return [(neighbor, self.pesos.get((vertex, neighbor), float('inf'))) 
                for neighbor in self.adj_list[vertex]]

    def obtener_peso(self, vertex_1, vertex_2):
        return self.pesos.get((vertex_1, vertex_2), float('inf'))

    def obtener_nodos(self):
        return list(self.adj_list.keys())

    def obtener_aristas(self):
        aristas = []
        for origen in self.adj_list:
            for destino in self.adj_list[origen]:
                if not self.dirigido and origen < destino:
                    aristas.append({
                        'origen': origen,
                        'destino': destino,
                        'peso': self.pesos[(origen, destino)]
                    })
        return aristas
