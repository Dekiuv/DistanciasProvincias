#Importamos libreria heapq.
from heapq import heapify, heappop, heappush
#Introducimos los datos en forma de diccionario.
graph = {
    "Barcelona": {"Tarragona": 1, "Girona": 1, "Lleida":2},
    "Tarragona": {"Barcelona": 1, "Lleida": 2, "Zaragoza": 5, "Teruel":6, "Castellon":4},
    "Girona": {"Barcelona": 1, "Lleida": 2},
    "Lleida": {"Barcelona": 2, "Tarragona": 2, "Girona": 2, "Huesca":1, "Zaragoza":4},
    "Huesca": {"Zaragoza": 2.5, "Lleida": 1},
    "Zaragoza": {"Teruel": 1.5, "Tarragona": 5, "Huesca":2.5},
    "Teruel": {"Castellon": 2, "Zaragoza": 1.5, "Tarragona": 6},
    "Castellon": {"Valencia": 2, "Teruel": 2, "Tarragona": 4},
    "Valencia": {"Alicante": 1.5, "Castellon": 2, "Teruel": 3},
    "Alicante": {"Valencia": 1.5}
   }

#Definimos la clase Graph
class Graph:
   # Inicializamos el atributo "graph".
   def __init__(self, graph: dict = {}):
       self.graph = graph
   
   def shortest_distances(self, source: str):
       #Iniciamos el valor de los nodos a infinito. 
       distances = {node: float("inf") for node in self.graph}
       #El origen le ponemos valor 0.
       distances[source] = 0
       # Inicializamos la cola de prioridad.
       # La prioridad inicial es 0 para el nodo 'source'.
       pq = [(0, source)]
       # Convierte la lista 'pq' en un heap (montículo binario) para que el elemento con
       # la prioridad más baja esté siempre en la primera posición.
       heapify(pq)
       # Inicializamos un conjunto vacío llamado para saber los nodos que ya se han visitados.
       visited = set()
       #Mientras la cola de prioridad no este vacia
       while pq:
          # Extraemos el nodo con la distancia más baja de la cola de prioridad.
          current_distance, current_node = heappop(pq)
          # Si el nodo que estemos ya ha sido visitado, lo saltamos.
          if current_node in visited:
            continue
          # Marcamos el nodo actual como visitado.
          visited.add(current_node)
          for neighbor, weight in self.graph[current_node].items():
            #Calculamos la distancia entre el nodo donde estemos hasta el vecino.
            tentative_distance = current_distance + weight
            # Si la distancia calculada es menor que la distancia almacenada actualmente para el vecino,
            # actualizamos la distancia y añadimos el vecino a la cola de prioridad.
            if tentative_distance < distances[neighbor]:
                distances[neighbor] = tentative_distance
                heappush(pq, (tentative_distance, neighbor))
       #Devolvemos el diccionario "distences"
       return distances

menu=False
while not menu:
  #Mostramos y preguntamos al usuario que ciudad quiere.
  print("Ciudades disponibles:", ", ".join(graph.keys()))
  usuario = input("Introduce el nombre de la ciudad de origen: ")
  # Verificamos si la ciudad introducida está en el diccionario 'graph'
  if usuario not in graph:
    print("Ciudad no encontrada. Por favor, intenta de nuevo.")
  else:
    # Si la ciudad es válida, crea el objeto 'Graph' y muestra las distancias más cortas
    G = Graph(graph=graph)
    print(G.shortest_distances(usuario))
    # Finaliza el bucle ya que se ha encontrado una ciudad válida
    menu = True