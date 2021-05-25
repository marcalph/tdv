from collections import deque

def iterative_bfs(graph, vertex, seen):
    q = deque()
    seen.add(vertex)
    q.append(vertex)
    while q:
        v = q.popleft()
        print(v)
        for nei in v.neighbors:
            if nei not in seen:
                q.append(nei)
                seen.add(nei)


def recursive_bfs(graph, q, seen):
    #base case
    if not q:
        return
    
    v = q.popleft()
    print(v)
    for nei in v.neighbors:
        if nei not in seen:
            q.append(nei)
            seen.add(nei)
    recursive_bfs(graph, q, seen)



