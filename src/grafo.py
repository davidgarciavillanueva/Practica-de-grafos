class Grafo:
    def __init__(self, dirigido=False):
        self.nodos = {}
        self.aristas = []
        self.dirigido = dirigido
    
    def agregar_nodo(self, id_nodo, nombre, ubicacion):
        """Agrega un nodo al grafo"""
        self.nodos[id_nodo] = {
            'nombre': nombre,
            'ubicacion': ubicacion
        }
    