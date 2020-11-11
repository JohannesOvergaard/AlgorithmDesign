from copy import copy, deepcopy

class Node(object):
    def __init__(self, config):
        self.id = config[0]
        self.is_red = len(config) == 2
        self.neighbors = []
        self.value = float('inf')

    def set_neighbor(self, n):
        self.neighbors.append(n)

    def edge_to(self, node):
        for neighbor in self.neighbors:
            if neighbor.destination == node:
                return neighbor
        return None
    
    def __lt__(self, other):
        return True
    
    def __str__(self):
        #return str(self.id)
        s = f"{self.id}\n"
        for neighbor in self.neighbors:
            s += f"-- {neighbor}\n"
        return s

class Edge(object):
    def __init__(self, u, v):
        self.source = u
        self.destination = v
        self.capacity = 1

    def decrease_capacity(self, delta):
        self.capacity -= delta
        reverse = self.destination.edge_to(self.source)
        if reverse is None:
            edge = Edge(self.destination, self.source)
            edge.capacity = 0
            self.destination.neighbors.append(edge)
            reverse = edge
        reverse.capacity += delta

    def __lt__(self, other):
        return -self.capacity < -other.capacity

class Graph(object):
    def __init__(self, s, t, all_edges, n, nodes, directed):
        self.s = s
        self.t = t
        self.all_edges = all_edges
        self.n = n
        self.nodes = [nodes[key] for key in nodes]
        self.directed = directed
        
    def printGraph(self):
        for n in self.nodes: 
            print(n)
            print(n.neighbors[0].destination)

    def flow_graph(self):
        graph_cp = deepcopy(self)

        for node in graph_cp.nodes:
            out_node = copy(node)
            # Neighbors is now a list of edges; not nodes
            out_node.neighbors = [Edge(out_node, v) for v in out_node.neighbors]
            node.neighbors = [Edge(node, out_node)]

        # Connect s and t out-nodes to new super sink
        super_sink = Node(["super_sink"])
        s_out = graph_cp.s.neighbors[0].destination
        t_out = graph_cp.t.neighbors[0].destination
        s_out.neighbors.append(Edge(s_out, super_sink))
        t_out.neighbors.append(Edge(t_out, super_sink))

        graph_cp.t = super_sink
        graph_cp.s = None

        return graph_cp
