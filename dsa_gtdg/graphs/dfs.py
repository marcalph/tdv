
def iterative_dfs(graph, v, seen):
    stack = []
    stack.append(v)
    while stack:
        v = stack.pop()
        if v in seen:
            continue
        
        seen.add(v)
        print(v)
        for nei in v.neighbors:
            if nei not in seen:
                stack.append(nei)


def recursive_dfs(graph, v, seen):
    seen.add(v)
    print(v)
    for nei in v.neighbors:
        if nei not in seen:
            recursive_dfs(graph, nei, seen)