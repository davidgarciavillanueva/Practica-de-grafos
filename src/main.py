from grafo import GraphList
from arbol_expansion import kruskal
from backtracking import OptimizadorRutas

def main(): 
    print(" OPTIMIZACIÓN DE RUTAS DE ENTREGA \n")
    

    
    # Crear el grafo (no dirigido = rutas bidireccionales)
    grafo = GraphList(dirigido=False)
    

    grafo.agregar_nodo('A', 'Sede Norte')
    grafo.agregar_nodo('B', 'Sede Sur')
    grafo.agregar_nodo('C', 'Sede Este')
    grafo.agregar_nodo('D', 'Sede Oeste')
    grafo.agregar_nodo('E', 'Sede Centro')
    grafo.agregar_nodo('F', 'Sede Industrial')
    
 # Formato: (origen, destino, distancia_km, costo_combustible)
    rutas = [
        ('A', 'B', 17, 3.5),  
        ('A', 'C', 60, 3.5),
        ('A', 'D', 28, 3.5),
        ('B', 'C', 92, 3.5),
        ('B', 'E', 9, 3.5),
        ('C', 'D', 75, 3.5),
        ('C', 'E', 22, 3.5),
        ('D', 'F', 18, 3.5),
        ('E', 'F', 110, 3.5)
    ]
    
    for origen, destino, distancia, costo_combustible in rutas:
        grafo.agregar_arista(origen, destino, distancia, costo_combustible)

    print("✅ Grafo creado correctamente")
    print(f"📊 {grafo.size} sedes: {grafo.obtener_nodos()}\n")