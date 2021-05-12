# O(mn) spacetime
def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
    n = len(mat)
    m = len(mat[0])
        
    moves = [(-1, 0), # up
                (+1, 0), # down 
                (0, -1), # left
                (0, +1)] # right
    
    dist = [[float("inf") for _ in range(m)] for _ in range(n)]
    q = []
    
    def bfs():
        while q: # is not empty
            row, col = q.pop(0)
            for mv in moves:
                nr, nc = row+mv[0], col+mv[1]       # updated coords
                if nr>=0 and nr<n and nc>=0 and nc<m:  # check for valid coords
                    if dist[nr][nc]>dist[row][col]+1 : 
                        dist[nr][nc]=dist[row][col]+1   
                        q.append((nr, nc))              # continue on same island

    for i in range(n):
        for j in range(m):
            if mat[i][j]==0:
                dist[i][j]=0
                q.append((i,j))
    print(q)
    bfs()
    return dist