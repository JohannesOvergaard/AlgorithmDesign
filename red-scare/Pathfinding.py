import queue
from Graph import *

def bfs2(s, filt, end_condition, reAddRed=False, visited = {}, q = queue.Queue()):
    
    if s not in visited:
        visited[s] = None
    for n in s.neighbors:
        if n not in visited and  filt(s, n):
            q.put((s,n))

    while not q.empty():
        u,v = q.get()
        visited[v] = u 
        for n in v.neighbors:
            if n not in visited and filt(v,n):
                q.put((v,n))
            elif reAddRed and n.is_red:
                q.put((v,n))
        
        if end_condition(v):
            path, curr = [v], v
            while curr != s:
                path.append(visited[curr])
                curr = visited[curr]
            path.reverse()
            return path, visited, q
    
    return None, visited, q

def bfs(G, filt):
    s, t = G.s, G.t
    visited = {}
    q = queue.Queue()

    for n in G.s.neighbors:
        if filt(s, n):
            q.put((s,n))

    while not q.empty():
        u,v = q.get()
        visited[v] = u 
        for n in v.neighbors:
            if n not in visited and filt(v,n):
                q.put((v,n))
        if v == t:
            path, curr = [t], t
            while curr != s:
                path.append(visited[curr])
                curr = visited[curr]
            path.reverse()
            return path
    
    return None

def dijkstra(G, cost):
    s, t = G.s, G.t
    visited = {}
    q = queue.PriorityQueue()

    for n in G.s.neighbors:
        q.put((cost(s, n), s, n))

    while not q.empty():
        c, u, v = q.get()
        visited[v] = (u, c) 
        for n in v.neighbors:
            if n not in visited or n == t:
                q.put((cost(v, n) + c, v, n))
        if v == t:
            path, curr = [t], t
            while curr != s:
                path.append(visited[curr][0])
                curr = visited[curr][0]
            path.reverse()
            return path
    
    return None

red_unreachable = set()
def dfs(n: Node, t: Node, visited: set,found_red) -> list :
    v = visited.copy()
    v.add(n)
    if n == t:
        if found_red: return [n]
        red_unreachable.update(v)
        return None
    
    for neighbor in n.neighbors:
        if neighbor not in v:
            fr = found_red or n.is_red
            path:list = dfs(neighbor, t, v, fr)
            if path is not None:
                path.append(n)
                return path
    return None

