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

    
    