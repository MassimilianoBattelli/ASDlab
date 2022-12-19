import os
import json

import numpy as np

import Graph
import igraph as ig
import matplotlib.pyplot as plt
import collections


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    if not start in visited:
        visited.add(start)
        print(f"Visited {start}")
    lstAdj = graph.getAdjList(start)
    for next in set(lstAdj) - visited:
        dfs(graph, next, visited)
    return visited


def dijkstra(graph, root):
    n = graph.n
    # initialize pred and distances
    pred = [.1 for _ in range(n)]
    dist = [np.Inf for _ in range(n)]
    dist[root] = 0
    pred[root] = root
    # initialize list of visited nodes
    expanded = [False for _ in range(n)]
    # main loop, all nodes
    for _ in range(n):
        # look for an unexpanded, least cost node
        u = -1
        for i in range(n):
            if not expanded[i] and (u == -1 or dist[i] < dist[u]):
                u = i
        # all the reachable nodes have been expanded
        if dist[u] == np.Inf:
            break
        expanded[u] = True
        # relax
        for v, cost in graph.getAdjList(u):
            if dist[u] + cost < dist[v]:
                dist[v] = dist[u] + cost
                pred[v] = u
    return dist, pred


if __name__ == "__main__":

    # ----- Read Json and show as adj list -----
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with open('./data/graph1.json', encoding='utf-8-sig') as jfile:
        jgraph = json.load(jfile)
        print(jgraph['name'])

    G = Graph.Graph(isDirected=jgraph['isDirected'])

    for n in jgraph['nodes']:
        G.addNode(n)

    for m in jgraph['arcs']:
        G.addEdge(m['end1'], m['end2'], (m['weight'] if "weight" in m.keys() else 1))

    print("\nPrinting Adjacent list:")
    G.printAdjlists()
    print("\nGet AdjList of node '1'")
    print(G.getAdjList(1))
    # ----- Execute algorithm on adj list -----

# ----- Show graph -----
g = ig.Graph(directed=True)
g.add_vertices(6)
g.add_edges([(0, 1), (1,0), (0,2), (1,2), (2,1), (1,3), (2,3),(3,2),(2,4),(4,2),(3,5),(4,5)])
# Generate the graph with its capacities
g.vs["name"] = ["s", "v1", "v2", "v3", "v4", "t"]
g.es["weight"] = [12,4,13,10,4,8,4,5,10,4,20,4]
g.es["width"] = [1, 1, 1, 1, 1, 1, 1]  # drawing width of each edge
g.es["color"] = ['#666', '#666', '#666', '#666', '#666', '#666', '#666']
grid = [[0, 2], [2, 4], [2, 0], [4, 4], [4, 0], [6, 2]]
fig, ax = plt.subplots()
ig.plot(
    g,
    target=ax,
    layout=grid,
    vertex_size=0.5,
    vertex_color='lightgreen',
    vertex_label=g.vs['name'],
    edge_width=g.es['width'],
    edge_label=g.es["weight"],
    edge_color=g.es["color"],
    edge_align_label=True,
    edge_background='white'
)

print("-----------------------")

print(dijkstra(G, 0))
plt.show()
