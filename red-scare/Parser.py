from sys import stdin
from Graph import *

def parse() -> Graph:
    num_nodes, num_edges, _ = map(int, input().rsplit())
    s, t = input().rsplit()
    nodes = {}

    for _ in range(num_nodes):
        n = Node(input().rsplit())
        nodes[n.id] = n

    for _ in range(num_edges):
        n1, e, n2 = input().rsplit()
        n1, n2 = nodes[n1], nodes[n2]
        n1.set_neighbor(n2)
        if e == "--":
            n2.set_neighbor(n1)

    s, t = nodes[s], nodes[t]
    return Graph(s, t)
