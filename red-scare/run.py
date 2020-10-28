from Parser import parse
from BFS import *
from Graph import *
import sys

sys.setrecursionlimit(25000000)

def noneProblem(G):
    p = bfs(G, lambda x, y: not y.is_red or y == G.t)
    #for n in p: print(n.id)
    return -1 if p is None else len(p)

def alternating(G):
    p = bfs(G, lambda x, y: x.is_red != y.is_red)
    #for n in p: print(n.id)
    return p != None

def some(G: Graph):
    p = dfs(G.s,G.t,set(),False)
    # print(p)
    return p != None


G = parse()

# print(noneProblem(G))
# print(alternating(G))
print(some(G))