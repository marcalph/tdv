def openLock(self, deadends: List[str], target: str) -> int:
    """ XXX is a lock combination
    
    """
    start = "0000"
    moves = [+1, -1]
    queue = [(start,0)]
    def neighbors(combination):
        """ takes a lock combination & returns
            possible neighbors for 1 slot step
        """
        res = []
        for idx in range(len(combination)):
            d = int(combination[idx])
            for mv in moves:
                nd = (d+mv)%10
                yield combination[:idx] + str(nd) + combination[idx+1:]
    
    
    viewed = set(["0000"])
    while queue: # is not empty
        cur_combination, cur_depth = queue.pop(0)    
        for nei in neighbors(cur_combination):
            if nei==target:
                return cur_depth
            if nei in deadends:
                continue
            else:
                if nei not in viewed:
                    viewed.add(nei)
                    queue.append((nei, cur_depth+1)
    return -1