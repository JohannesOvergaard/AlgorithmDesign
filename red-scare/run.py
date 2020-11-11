import sys
import copy

from Parser import parse
from Graph import Graph, Edge, Node
from Pathfinding import bfs, dfs, dijkstra, bellman_ford
from Flow import max_flow

sys.setrecursionlimit(2500000)

def none(G):
    p = bfs(G, lambda x, y: not y.is_red or y == G.t)
    #for n in p: print(n.id)
    return -1 if p is None else len(p)

def many(G):
    if not G.directed:
        return "cycles stop us"
    t_value = bellman_ford(G)
    if t_value == - float("inf"):
        return "cycles stop us"
    if t_value == float("inf"):
        return "t is not attached to s"
    return abs(t_value)

def few(G):
    p = dijkstra(G, lambda x, y: 1 if y.is_red else 0)
    return -1 if p is None else len([x for x in p if x.is_red])

def alternating(G):
    p = bfs(G, lambda x, y: x.is_red != y.is_red)
    #for n in p: print(n.id)
    return p != None

def some(G: Graph):
    if G.s.is_red or G.t.is_red:
        p = bfs(G, lambda x, y:True)
        return p is not None
    if G.directed:
        val = many(G)
        if type(val) != str and val > 0:
            return True
        return False

    for i in range(len(G.nodes)):
        if not G.nodes[i].is_red: continue
        fg = G.flow_graph()
        node = fg.nodes[i]
        super_source = Node(["super_source"])
        edge = Edge(super_source, node)
        edge.capacity = 2
        super_source.neighbors.append(edge)
        node.neighbors[0].capacity = 2
        fg.s = super_source        
        if max_flow(fg) == 2: return True
    return False

G = parse()
print("Alternating:", alternating(G))
print("Few:", few(G))
print("Many:", many(G))
print("None:", none(G))
print("Some:", some(G))
print()
