class Node(object):
    def __init__(self, config):
        self.id = config[0]
        self.is_red = len(config) == 2
        self.neighbors = []

    def set_neighbor(self, n):
        self.neighbors.append(n)
    
    def __lt__(self, other):
        return True
    
    def __str__(self):
        return str(self.id)
        s = f"{self.id}\n"
        for neighbor in self.neighbors:
            s += f"-- {neighbor.id}\n"
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
    def __init__(self, s, t):
        self.s = s
        self.t = t
