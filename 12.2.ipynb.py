import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
for node in (1, 2, 3, 5, 6):
    G.add_node(node)
for (a, b) in [(1,2),(2,3),(3,4),(4,5),(5,6),(6,1),(1,3),(3,5),(1,5)]:
    G.add_edge(a, b)
nx.draw(G)
plt.show()
