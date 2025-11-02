class GraphList:
    
    def __init__(self, dirigido=False):
        self.adj_list = {}
        self.pesos = {}
        self.info_nodos = {}
        self.size = 0
        self.dirigido = dirigido

    def agregar_nodo(self, value, nombre=""):
        """Agrega un nodo al grafo"""
        if value in self.adj_list:
            return None
        self.adj_list[value] = []
        self.info_nodos[value] = {'nombre': nombre}
        self.size += 1

    def agregar_arista(self, vertex_1, vertex_2, distancia, costo_combustible):
        """Agrega una arista con peso calculado"""
        if vertex_1 not in self.adj_list:
            self.agregar_nodo(vertex_1)
        if vertex_2 not in self.adj_list:
            self.agregar_nodo(vertex_2)

        # Agregar arista
        if vertex_2 not in self.adj_list[vertex_1]:
            self.adj_list[vertex_1].append(vertex_2)
            self.pesos[(vertex_1, vertex_2)] = peso

        if not self.dirigido and vertex_1 not in self.adj_list[vertex_2]:
            self.adj_list[vertex_2].append(vertex_1)
            self.pesos[(vertex_2, vertex_1)] = peso
        
         # Calcular peso
        peso = self._calcular_peso(distancia, costo_combustible)

    
    def _calcular_peso(self, distancia, costo_combustible):
        """Calcula el peso basado en distancia y combustible"""
        galones = distancia / 10
        return galones * costo_combustible


    def obtener_vecinos(self, vertex):
        """Retorna lista de (vecino, peso)"""
        vecinos = []
        for neighbor in self.adj_list[vertex]:
            peso = self.pesos.get((vertex, neighbor), float('inf'))
            vecinos.append((neighbor, peso))
        return vecinos


    def obtener_peso(self, vertex_1, vertex_2):
        """Obtiene el peso entre dos nodos"""
        return self.pesos.get((vertex_1, vertex_2), float('inf'))