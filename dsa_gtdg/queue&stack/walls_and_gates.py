class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # constants
        GATE = 0
        WALL = -1
        m = len(rooms)
        if m==0: # empty input
            return
        n = len(rooms[0])
        q = []
        
        # get gates
        for i in range(m):
            for j in range(n):
                if rooms[i][j]!=GATE:
                    continue
                else:
                    q.append((i,j))
        
        moves = [
            (-1,0), # up
            (+1,0), # down
            (0,-1), # left
            (0,+1), # right
        ]
        step = 0
        while q: # is not empty
            row, col = q.pop(0)
            for vert, hor in moves:
                r, c = row+vert, col+hor
                if r<0 or r>=m or c<0 or c>=n or rooms[r][c]!=2147483647:
                    continue
                else:
                    rooms[r][c]=rooms[row][col]+1
                    q.append((r,c))