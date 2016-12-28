"""
Solution to Euler Problem number 18.
We use a DAG with negative edge weights.
"""
from helpers import open_local_file
import networkx as nx

FILE = open_local_file('data.txt').read()
G = nx.DiGraph()

# Set up the pyramid data
FILE = FILE.split('\n')
for i in range(0,len(FILE)):
    FILE[i] = FILE[i].split()

children = [1]
for l, row in enumerate(FILE):
    node_num = max(children) + 1
    
    for x in row:
        if (l != len(FILE) - 1):
            parent = children.pop(0)

            G.add_edge(parent, node_num, weight=-int(x))
            if node_num not in children:
                children.append(node_num)

            node_num += 1

            G.add_edge(parent, node_num, weight=-int(x))
            if node_num not in children:
                children.append(node_num)

for child, w in zip(children, FILE[-1]):
    G.add_edge(child, 0, weight=-int(w))

pred, dist = nx.bellman_ford(G, 1)
print - dist[0]