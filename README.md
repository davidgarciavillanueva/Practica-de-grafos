# 🚚 Optimización de Rutas de Entrega

## 📘 Descripción del proyecto
Este proyecto implementa un sistema para optimizar rutas de entrega entre diferentes sedes de una empresa, utilizando **estructuras de grafos** y **algoritmos clásicos de optimización**.  

El sistema modela las sedes como **nodos** y las rutas entre ellas como **aristas** ponderadas según su costo o distancia.  
Se aplican dos algoritmos principales:

1. **Kruskal (Árbol de Expansión Mínimo)**  
   Encuentra la forma más económica de conectar todas las sedes minimizando el costo total de infraestructura (por ejemplo, carreteras o conexiones de transporte).

2. **Backtracking Iterativo (Ruta Óptima)**  
   Calcula una ruta completa que recorra todas las sedes y regrese al punto inicial, buscando el costo total más bajo posible.  
   Este proceso simula la optimización de una ruta diaria de distribución.

El programa finalmente muestra un análisis comparativo entre:
- El costo mínimo de conexión (Kruskal),
- El costo de la mejor ruta de entrega (Backtracking),
- Y el ahorro obtenido frente a conectar todas las rutas posibles.

---

##  Cómo ejecutar el proyecto

### 1️⃣ Requisitos previos
- Tener instalado **Python 3.10+**
- Tener los archivos del proyecto organizados en una estructura como esta:

  ```plaintext
  Practica-de-grafos/
  ├── src/
  │   ├── main.py
  │   ├── grafo.py
  │   ├── arbol_expansion.py
  │   └── backtracking.py

### 2️⃣ Ejecución

1. Abre una terminal o consola en la carpeta del proyecto (`src` o el directorio raíz).

2. Ejecuta el siguiente comando:

   ```bash
   python src/main.py

El programa mostrará en consola:

- El grafo creado con todas las sedes.  
- Las rutas esenciales del **Árbol de Expansión Mínimo (Kruskal)**.  
- La **Ruta Óptima** generada por el algoritmo de **Backtracking**.  
- Un resumen del análisis de costos y ahorro obtenido.  

##  Supuestos asumidos

- El grafo es **no dirigido**, es decir, las rutas son bidireccionales (A → B equivale a B → A).  
- Los costos o distancias entre sedes son **simétricos** (el costo de ir y volver es el mismo).  
- No existen rutas negativas ni nulas.  
- Todos los nodos (sedes) están conectados al menos indirectamente.  
- El algoritmo de **Backtracking** busca la mejor ruta completa partiendo desde una sede inicial (por defecto, la sede ‘A’).  
- El modelo no considera variables externas como tráfico, clima o restricciones horarias; se enfoca únicamente en **distancia y costo**.  
