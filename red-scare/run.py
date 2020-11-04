import sys

from Parser import parse
from Graph import *
from Pathfinding import *

sys.setrecursionlimit(25000000)

def none(G):
    p = bfs(G, lambda x, y: not y.is_red or y == G.t)
    #for n in p: print(n.id)
    return -1 if p is None else len(p)


def many(G):
    t_value = bellManFord(G)
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
    p, contains_red = dfs(G.s,G.t)
    print(f'Found red: {contains_red}')
    for v in p:
        print(v.id)
    return len(p) > 0 and contains_red


G = parse()
# print(none(G))
# print(alternating(G))
# print(few(G))
#print(some(G))
print(many(G))
