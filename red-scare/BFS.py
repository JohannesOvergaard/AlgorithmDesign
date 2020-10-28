import queue
from Graph import Graph, Node

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

# def bfs(n: Node, t: Node, visited: set, q):
#     visited.add(n)
#     if n == t: return [n]
#     for neighbor in n.neighbors:
#         if neighbor in visited: continue
#         path = bfs(neighbor, t, visited)
#         if path is not None:
#             path.append(n)
#             return path
#     return None

def dfs(n: Node, t: Node, visited: set,found_red) -> list :
    v = visited.copy()
    v.add(n)
    if n == t:
        if found_red: return [n]
        return None
    
    for neighbor in n.neighbors:
        if neighbor not in v:
            fr = found_red or n.is_red
            path:list = dfs(neighbor, t, v, fr)
            if path is not None:
                path.append(n)
                return path
    return None
