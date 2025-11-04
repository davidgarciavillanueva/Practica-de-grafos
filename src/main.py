from grafo import GraphList
from arbol_expansion import UnionFind
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

    print("1. ÁRBOL DE EXPANSIÓN MÍNIMO (Kruskal):")
    arbol_kruskal, costo_kruskal = UnionFind.kruskal(grafo)
    print(f"   Costo total: ${costo_kruskal:.2f}")
    print("   Rutas esenciales:")
    for arista in arbol_kruskal:
        info_origen = grafo.obtener_info_nodo(arista['origen'])
        info_destino = grafo.obtener_info_nodo(arista['destino'])
        print(f"     {arista['origen']} -> {arista['destino']}: ${arista['peso']:.2f}")
    print()

    # ==================== BACKTRACKING ITERATIVO - RUTA ÓPTIMA ====================
    print("2. BACKTRACKING ITERATIVO - RUTA ÓPTIMA:")
    optimizador = OptimizadorRutas(grafo)
    ruta_optima, costo_optimo = optimizador.encontrar_ruta_optima('A')

    print(f"   Ruta encontrada: {' -> '.join(ruta_optima)}")
    print(f"   Costo total: ${costo_optimo:.2f}")

    # Mostrar detalles del recorrido
    print("\n   Detalle del recorrido:")
    for i in range(len(ruta_optima) - 1):
        origen = ruta_optima[i]
        destino = ruta_optima[i + 1]
        peso = grafo.obtener_peso(origen, destino)
        info_origen = grafo.obtener_info_nodo(origen)
        info_destino = grafo.obtener_info_nodo(destino)
        print(f"     {origen} -> {destino}: ${peso:.2f}")
    print()

    # ==================== ANÁLISIS DE RESULTADOS ====================
    print("3. ANÁLISIS:")
    print(f"   • Sedes conectadas: {grafo.size}")
    print(f"   • Costo infraestructura mínima: ${costo_kruskal:.2f}")
    print(f"   • Costo ruta diaria óptima: ${costo_optimo:.2f}")

    # Calcular ahorro vs conectar todas las rutas
    costo_total_todas_rutas = sum(arista['peso'] for arista in grafo.obtener_aristas())
    ahorro = costo_total_todas_rutas - costo_kruskal
    print(f"   • Ahorro vs conectar todo: ${ahorro:.2f}\n")

    # ==================== EXPLICACIÓN DE ALGORITMOS ====================
    print("4. EXPLICACIÓN DE ALGORITMOS:")
    print("   • GraphList: Modela el grafo con lista de adyacencia")
    print("   • Kruskal: Encuentra conexión mínima entre todas las sedes")
    print("   • Backtracking Iterativo: Encuentra ruta óptima usando pila")
    print("   • Los algoritmos garantizan soluciones óptimas")

if __name__ == "__main__":
    main()