class Node(object):
    def __init__(self, config):
        self.id = config[0]
        self.is_red = len(config) == 2
        self.neighbors = []
        self.value = float('inf')

    def set_neighbor(self, n):
        self.neighbors.append(n)
    
    def __lt__(self, other):
        return True
    
    def __str__(self):
        #return str(self.id)
        s = f"{self.id} v={self.value}\n"
        #for neighbor in self.neighbors:
        #    s += f"-- {neighbor.id}\n"
        return s
"""
class Edge(object):
    def __init__(self, u, v, c):
        self.source = u
        self.destination = v
        self.capacity = c if c != -1 else float('inf')
        self.reverse = None

    def __lt__(self, other):
        return -self.capacity < -other.capacity

    def __str__(self):
        return f"{self.source} {self.destination} {int(self.reverse.capacity / 2)}"
"""

class Graph(object):
    def __init__(self, s, t, allEdges, n, nodes):
        self.s = s
        self.t = t
        self.allEdges = allEdges
        self.n = n
        self.nodes = [nodes[key] for key in nodes]
        
    def printGraph(self):
        for n in self.nodes:
            print(n)
