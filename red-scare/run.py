from Parser import parse
from Pathfinding import bfs, dijkstra

def none(G):
    p = bfs(G, lambda x, y: not y.is_red or y == G.t)
    #for n in p: print(n.id)
    return -1 if p is None else len(p)

def some(G): pass

def many(G): pass

def few(G):
    p = dijkstra(G, lambda x, y: 1 if y.is_red else 0)
    return -1 if p is None else len([x for x in p if x.is_red])

def alternating(G):
    p = bfs(G, lambda x, y: x.is_red != y.is_red)
    #for n in p: print(n.id)
    return p != None

G = parse()
print(none(G))
print(alternating(G))
print(few(G))
print(some(G))
