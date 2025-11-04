class OptimizadorRutas:
    def __init__(self, grafo):
        self.grafo = grafo
        self.mejor_ruta = None
        self.mejor_costo = float('inf')
      
    def encontrar_ruta_optima(self, inicio):
