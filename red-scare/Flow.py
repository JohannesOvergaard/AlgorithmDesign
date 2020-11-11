from heapq import heappop, heappush

def st_path(G):
    s, t = G.s, G.t
    explored = {}
    frontier = []
    for e in s.neighbors:
        heappush(frontier, e)
    while frontier != []:
        curr = heappop(frontier)
        if curr.capacity == 0: continue
        if curr.destination in explored:
            continue
        explored[curr.destination] = curr
        for e in curr.destination.neighbors:
            heappush(frontier, e)
        if t in explored:
            lst = []
            curr = t
            while(curr != s):
                lst.append(explored[curr])
                curr = explored[curr].source
            lst.reverse()
            return lst, False # False means "not done" with FF
    return explored, True # True means "done" with FF

def bottleneck(path):
    return min([e.capacity for e in path])

def augment(path):
    b = bottleneck(path)
    for e in path:
        e.decrease_capacity(b)

def max_flow(G):
    explored, is_done = st_path(G)
    while is_done is False:
        augment(explored)
        explored, is_done = st_path(G)
    return sum([e.capacity for e in G.t.neighbors])
