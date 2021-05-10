class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """ find # of islands in grid
        """
        # boring constants
        n, p = len(grid), len(grid[0])
        count = 0
        moves = [(-1, 0), # up
                 (+1, 0), # down 
                 (0, -1), # left
                 (0, +1)] # right
        
        
        def bfs(grid, row, col):
            # bfs queue
            q = []
            q.append((row,col))                         
            grid[row][col]=0
            while q: # is not empty
                row, col = q.pop(0)
                for mv in moves:
                    nr, nc = row+mv[0], col+mv[1]       # updated coords
                    if nr<0 or nr>=n or nc<0 or nc>=p:  # check for valid coords
                        continue
                    elif grid[nr][nc]=="1": 
                        q.append((nr, nc))              # continue on same island
                        grid[nr][nc]="0"                  # do not look back
        
        def dfs(grid, row, col):
            if row<0 or row>=n or col<0 or col>=p or grid[row][col]=="0":  # check for valid coords
                return None
            
            grid[row][col]="0"
            dfs(grid, row+1, col)
            dfs(grid, row-1, col)
            dfs(grid, row, col+1)
            dfs(grid, row, col-1)
                
        for i in range(n):
            for j in range(p):
                if grid[i][j]=="1":
                    bfs(grid, i, j)
                    count+=1
        return count