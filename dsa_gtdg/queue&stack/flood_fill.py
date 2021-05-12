# O(n) spacetime
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """ todo
        """
        # vardef
        n = len(image)
        m = len(image[0])
        queue = [(sr, sc)]
        starting_color = image[sr][sc]
        print(starting_color)
        moves = [(+1, 0),   # down
                 (-1, 0),   # up
                 (0, +1),   # right
                 (0, -1)]   # left
        if starting_color!=newColor:
            while queue:
                row, col = queue.pop(0)
                image[row][col]= newColor
                for mv in moves:
                    nrow, ncol = row + mv[0], col + mv[1]
                    if 0<=nrow<n and 0<=ncol<m:
                        if image[nrow][ncol]==starting_color:
                            queue.append((nrow, ncol))
        return image
    