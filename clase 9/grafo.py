import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo vacío
G = nx.Graph()

# Agregar nodos
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)

# Agregar aristas
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 1)

# Obtener la cantidad de nodos y aristas
num_nodos = G.number_of_nodes()
num_aristas = G.number_of_edges()

print(f"El grafo tiene {num_nodos} nodos y {num_aristas} aristas.")

# Dibujar el grafo
pos = nx.spring_layout(G)  # Posiciones para el dibujo
nx.draw(G, pos, with_labels=True, node_size=500)
plt.show()
