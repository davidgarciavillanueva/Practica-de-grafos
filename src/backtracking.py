class OptimizadorRutas:
    def __init__(self, grafo):
        self.grafo = grafo
        self.mejor_ruta = None
        self.mejor_costo = float('inf')
      
    def encontrar_ruta_optima(self, inicio):
        nodos = self.grafo.obtener_nodos()
        nodos.remove(inicio)
        
        # Pila para simular la recursión: (ruta, visitados, costo, nodos_restantes)
        pila = [(
            [inicio],           # ruta_actual
            {inicio},           # visitados
            0,                  # costo_actual
            nodos.copy()        # nodos_restantes
        )]
        
        while pila:
            ruta_actual, visitados, costo_actual, nodos_restantes = pila.pop()

