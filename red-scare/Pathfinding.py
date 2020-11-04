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
            if n not in visited and filt(dfsv,n):
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


def bellManFord(G):
    s = G.s
    n = G.n
    v = len(G.allEdges)
    s.value =  0
    for i in range(n-1):
        for (u,v) in G.allEdges:        #(u,v)
            uv = u.value
            vv = v.value
            ecost = -1 if u.is_red else 0
            v.value = min(uv + ecost, vv)
    
    for i in range(n-1):
        for (u,v) in G.allEdges:        #(u,v)
            uv = u.value
            vv = v.value
            ecost = -1 if u.is_red else 0
            if uv + ecost < vv:
                v.value = - float("inf")
    return G.t.value            









# tail_recursion.py
# Boilerplate for doing actual tail recursion in python. Taken from https://chrispenner.ca/posts/python-tail-recursion
class Recurse(Exception):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


def recurse(*args, **kwargs):
    raise Recurse(*args, **kwargs)


def tail_recursive(f):
    def decorated(*args, **kwargs):
        while True:
            try:
                return f(*args, **kwargs)
            except Recurse as r:
                args = r.args
                kwargs = r.kwargs
                continue

    return decorated


def dfs(n: Node, t: Node) -> list:
    q = queue.LifoQueue()
    q.put(n)
    return dfs_helper(q, set(), set(), [], t, False)


@tail_recursive
def dfs_helper(stack: queue.LifoQueue, visited: set, visited_path: set, acc: list, t: Node, found_red: bool):
    if stack.empty():  # No path s-t, was found that contained a red node
        return [], found_red
    else:
        current: Node = stack.get()
        if current in visited and not found_red or current in visited_path:  # Not sure  if this check is correct :/
            recurse(stack, visited, visited_path, acc, t, found_red)
        elif current == t:  # Found the target node
            if found_red:  # Encountered a red node in the path
                acc.append(current)
                return acc, found_red
            else:
                path = path_until_last_branch(acc)  # Determines a what node the latest branching in the path occurred
                recurse(stack, visited, visited_path, path, t, found_red)
        else:
            for neighbor in current.neighbors:
                if neighbor not in visited or (found_red and current in visited_path):
                    stack.put(neighbor)
            if current.is_red:
                found_red = True
            acc.append(current)
            visited_path.add(current)
            visited.add(current)
            recurse(stack, visited, visited_path, acc, t, found_red)


def path_until_last_branch(path: list):
    length = len(path) - 1
    for i in range(length, 0, -1):
        if len(path[i].neighbors) > 1:
            return path[0:i]
    return []

    