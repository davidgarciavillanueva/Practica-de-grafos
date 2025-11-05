
class OptimizadorRutas:
    def __init__(self, grafo):
        
        self.grafo = grafo
        # Mejor ruta encontrada hasta ahora , inicialmente None
        self.mejor_ruta = None
        # Mejor costo encontrado; inicializamos a infinito para minimizar
        self.mejor_costo = float('inf')
      
    def encontrar_ruta_optima(self, inicio):
        # Obtener todos los nodos del grafo
        nodos = self.grafo.obtener_nodos()
        # Remover el nodo de inicio de la lista de nodos a visitar, ya que
        # la ruta parte desde 'inicio' y este se añadirá al final para cerrar el ciclo
        nodos.remove(inicio)
        
        # tupla: (ruta_actual, visitados, costo_actual, nodos_restantes)

        pila = [([inicio], {inicio}, 0, nodos.copy())]
        
        # Bucle principal: procesar hasta que la pila quede vacía
        while pila:
            # Sacar el último estado (LIFO)
            ruta_actual, visitados, costo_actual, nodos_restantes = pila.pop()
            
            # Caso base: si no quedan nodos por visitar, calcular el costo de regresar al inicio
            if not nodos_restantes:
                # Obtener el costo de la arista desde el último nodo de la ruta hasta el inicio
                costo_regreso = self.grafo.obtener_peso(ruta_actual[-1], inicio)
                #(ida + vuelta)
                costo_total = costo_actual + costo_regreso
                
                # Si encontramos una ruta mejor, actualizar mejor_ruta y mejor_costo
                if costo_total < self.mejor_costo:
                    # Guardamos la ruta completa incluyendo el retorno al inicio
                    self.mejor_costo = costo_total
                    self.mejor_ruta = ruta_actual + [inicio]
                # Continuar con el siguiente estado en la pila
                continue  
            
            # lleva la ruta actual a cada nodo restante
            # Usamos reversed para controlar el orden de expansión por la pila
            for nodo in reversed(nodos_restantes):
                # Obtener el costo de moverse desde el último nodo actual hasta el candidato
                costo_arista = self.grafo.obtener_peso(ruta_actual[-1], nodo)
                # Nuevo costo acumulado si tomamos esa arista
                nuevo_costo = costo_actual + costo_arista
                
                # Poda: solo expandimos si el costo parcial es menor que la mejor solución conocida
                if nuevo_costo < self.mejor_costo:
                    # Construir nuevos valores para el estado
                    nueva_ruta = ruta_actual + [nodo]
                    # Actualizar conjunto de visitados (operación no estrictamente necesaria aquí)
                    nuevos_visitados = visitados | {nodo}
                    # Construir una nueva lista de nodos restantes sin el nodo escogido
                    nuevos_nodos_restantes = [n for n in nodos_restantes if n != nodo]
                    
                    # Apilar el nuevo estado para procesarlo posteriormente
                    pila.append((
                        nueva_ruta,
                        nuevos_visitados,
                        nuevo_costo,
                        nuevos_nodos_restantes
                    ))
        
        
        return self.mejor_ruta, self.mejor_costo
