class OptimizadorRutas:
    def __init__(self, grafo):
        self.grafo = grafo
        self.mejor_ruta = None
        self.mejor_costo = float('inf')
      
    def encontrar_ruta_optima(self, inicio):
        nodos = self.grafo.obtener_nodos()
        nodos.remove(inicio)
        
        # Pila (ruta act, visitados, costo act, nodos_restantes)
        pila = [([inicio],{inicio},0,nodos.copy())]
        
        while pila:
            ruta_actual, visitados, costo_actual, nodos_restantes = pila.pop()
            
            # Caso base: todos los nodos visitados
            if not nodos_restantes:
                costo_regreso = self.grafo.obtener_peso(ruta_actual[-1], inicio)
                costo_total = costo_actual + costo_regreso
                
                if costo_total < self.mejor_costo:
                    self.mejor_costo = costo_total
                    self.mejor_ruta = ruta_actual + [inicio]
                continue  
            
            for nodo in reversed(nodos_restantes):
                costo_arista = self.grafo.obtener_peso(ruta_actual[-1], nodo)
                nuevo_costo = costo_actual + costo_arista
                
                if nuevo_costo < self.mejor_costo:
                    nueva_ruta = ruta_actual + [nodo]
                    nuevos_visitados = visitados | {nodo}
                    nuevos_nodos_restantes = [n for n in nodos_restantes if n != nodo]
                    
                    pila.append((
                        nueva_ruta,
                        nuevos_visitados,
                        nuevo_costo,
                        nuevos_nodos_restantes
                    ))
        
        return self.mejor_ruta, self.mejor_costo

