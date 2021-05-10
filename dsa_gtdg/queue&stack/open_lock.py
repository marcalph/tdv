#O(N^2          2N(neighbors)*N (string construction) 
#  * 10^N       number of potential neighbors to visit
#  + D) time    where N keys + D deadends hashset
# O(10^N)
def openLock(self, deadends: List[str], target: str) -> int:
    """ XXXX is a lock combination
    """
    def neighbors(node):
        for i in range(4):
            x = int(node[i])
            for d in (-1, 1):
                y = (x + d) % 10
                yield node[:i] + str(y) + node[i+1:]

    dead = set(deadends)
    queue = [('0000', 0)]
    seen = {'0000'}
    while queue:
        node, depth = queue.pop(0)
        if node == target: return depth
        if node in dead: continue
        for nei in neighbors(node):
            if nei not in seen:
                seen.add(nei)
                queue.append((nei, depth+1))
    return -1