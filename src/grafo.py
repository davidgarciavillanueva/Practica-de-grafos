# lista de adyacencia 
class GraphList:
    def __init__(self, dirigido=False):
        #  nodo ,lista  vecinos
        self.adj_list = {}
        #  (origen, destino) ysu peso 
        self.pesos = {}
        # cuenta nodos 
        self.size = 0
        self.dirigido = dirigido

    def agregar_nodo(self, value):
        # Añade un nodo si no existe
        if value in self.adj_list:
            # Si ya existe
            return None
        # crealista de adyacencia vacía para el nuevo nodo
        self.adj_list[value] = []
        
        self.size += 1

    def agregar_arista(self, vertex_1, vertex_2, distancia, costo_combustible):
        # Asegurarse de que ambos nodos existen en el grafo si nocrearlos
        if vertex_1 not in self.adj_list:
            self.agregar_nodo(vertex_1)
        if vertex_2 not in self.adj_list:
            self.agregar_nodo(vertex_2)


        peso = (distancia / 10) * costo_combustible
        
        # Si la arista (vertex_1 -> vertex_2) no está ya en la lista de adyacencia, añadirla
        if vertex_2 not in self.adj_list[vertex_1]:
            self.adj_list[vertex_1].append(vertex_2)
            # Guardar el peso en el diccionario de pesos con clave (origen, destino)
            self.pesos[(vertex_1, vertex_2)] = peso

        # la arista inversa (vertex_2 -> vertex_1)
        # con el mismo peso, pa no tener duplicados 
        if not self.dirigido and vertex_1 not in self.adj_list[vertex_2]:
            self.adj_list[vertex_2].append(vertex_1)
            self.pesos[(vertex_2, vertex_1)] = peso

    def obtener_vecinos(self, vertex):
        #lista de tuplas (vecino, peso) para un nodo x.
        # Si por alguna razón no hay peso registrado para (vertex, neighbor), se usa inf.
        return [(neighbor, self.pesos.get((vertex, neighbor), float('inf'))) 
                for neighbor in self.adj_list[vertex]]

    def obtener_peso(self, vertex_1, vertex_2):
        # Devuelve el peso de la arista (vertex_1, vertex_2) o infinito si no existe.
        return self.pesos.get((vertex_1, vertex_2), float('inf'))

    def obtener_nodos(self):
        # Devuelve la lista de nodos del grafo (claves del diccionario adj_list)
        return list(self.adj_list.keys())

    def obtener_aristas(self):
        #  devuelve una lista de aristas en forma de dict:
        # {'origen': ..., 'destino': ..., 'peso': ...}
        aristas = []
        for origen in self.adj_list:
            # Para cada destino/vecino del origen
            for destino in self.adj_list[origen]:
                # y se usa la comparación origen < destino para evitar duplicados 
                if not self.dirigido and origen < destino:
                    aristas.append({
                        'origen': origen,
                        'destino': destino,
                        'peso': self.pesos[(origen, destino)]
                    })
        return aristas
