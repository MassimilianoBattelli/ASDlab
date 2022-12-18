# node of adjacency list in weighted graph
class AdjNode:
    def __init__(self, data, weight=1):
        self.id = data
        self.next = None
        self.weight = weight


class Graph:
    def __init__(self, isDirected=True, isWeighted=False):
        self.n = self.m = 0
        self.roots = dict()  # roots of adjacency node lists
        self.nodes = dict()  # attributes of the nodes
        self.isDirected = isDirected
        self.isWeighted = isWeighted

    def addNode(self, node):
        if not node['id'] in self.roots:
            self.roots.update({node['id']: None})
            self.nodes.update({node['id']: (node['label'], node['x'], node['y'])})
            self.n += 1

    def addEdge(self, src, dest, weight=1):
        # Add the destination to the front of source node adjlist
        if not src in self.roots:
            self.roots.update({src: None})
            self.n += 1
        if not dest in self.roots:
            self.roots.update({dest: None})
            self.n += 1
        node = AdjNode(dest, weight)
        node.next = self.roots[src]
        self.m += 1
        self.roots[src] = node
        if self.isWeighted:
            print(f"Adding {src}->{node.id} cost {node.weight}")
        else:
            print(f"Adding {src}->{node.id}")

        if not self.isDirected:
            lst = self.getAdjList(dest)
            if not src in lst:
                node = AdjNode(src, weight)
                node.next = self.roots[dest]
                self.roots[dest] = node
                self.m += 1

    def getAdjList(self, node):
        adjList = []
        temp = self.roots[node]
        while temp:
            adjList.append((temp.id, temp.weight))
            temp = temp.next
        return adjList

    # Print all adjacency lists
    def printAdjlists(self):
        for kv in self.roots:
            print(f"Adjacency list of vertex {kv}\n head", end="")
            lst = self.getAdjList(kv)
            temp = self.roots[kv]
            while temp:
                if self.isWeighted:
                    print(f" -> ({temp.id},{temp.weight})", end="")
                else:
                    print(f" -> ({temp.id})", end="")
                temp = temp.next
            print(" \n")
