import sys

from Parser import parse
from Graph import *
from Pathfinding import bfs, bfs2, dijkstra, dfs
import queue

sys.setrecursionlimit(25000000)

def none(G):
    p = bfs(G, lambda x, y: not y.is_red or y == G.t)
    #for n in p: print(n.id)
    return -1 if p is None else len(p)

def compute_some(G): 
    if G.s.is_red or G.t.is_red:
        return bfs(G, lambda x, y: not y.is_red or y == G.t)

    filt     = lambda x, y: not x.is_red
    end_cond = lambda y: y.is_red
    filt2     = lambda x, y: True
    end_cond2 = lambda y: y == G.t
    p_s_r, visited, q = bfs2(G.s, filt, end_cond, reAddRed=True)
    while(p_s_r is not None):
        
        queueNew = queue.Queue()        #new queue because ot python bug with next call to bfs2 overriding q
        while(not q.empty()): queueNew.put(q.get())
        
        visited2 = {}
        for v in p_s_r:
            visited2[v] = None
        p_r_t, _, _ = bfs2(p_s_r[-1], filt2, end_cond2, reAddRed=False, visited = visited2)
        if p_r_t is None:            
            while(not queueNew.empty()): q.put(queueNew.get())
            p_s_r, visited, q = bfs2(G.s, filt, end_cond, reAddRed=True, visited = visited, q = q)
        else:
            p = p_s_r + p_r_t[1:]
            return p
            break
    return None

def many(G): pass

def few(G):
    p = dijkstra(G, lambda x, y: 1 if y.is_red else 0)
    return -1 if p is None else len([x for x in p if x.is_red])

def alternating(G):
    p = bfs(G, lambda x, y: x.is_red != y.is_red)
    #for n in p: print(n.id)
    return p != None

def some(G: Graph):
    p = compute_some(G)
    print(*p)
    return p != None


G = parse()
# print(none(G))
# print(alternating(G))
# print(few(G))
print(some(G))
