import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

fig, ax = plt.subplots()

G = nx.DiGraph()

nodes = np.arange(30)

edges = []

for node, i in enumerate(nodes):
	for x in nodes[:i]:
		edges.append((x, node))

print(edges)
	
options = {
	'node_color': 'white',
	'node_size': 200,
	'edge_color': 'red',
	'width': 0.5,
	'font_size': 12 
}

G.add_nodes_from(nodes)
G.add_edges_from(edges)
nx.draw_shell(G, with_labels=True, **options)
plt.show()
