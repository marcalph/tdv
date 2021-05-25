#O(rows*cols) spacetime 
def riverSizes(matrix):
    # Write your code here.
    rows = len(matrix)
	cols = len(matrix[0])
	
	res = []
	moves = [
		(+1, 0), # down
		(-1, 0), # up
		(0, +1), # right
		(0, -1), # left
	]
	
	def traverse(row, col, matrix):
		size=0
		q = []
		q.append((row,col))
		matrix[row][col] = 0
		size += 1
		while q:
			coords = q.pop(0)
			for mv in moves:
				newcoords = coords[0] + mv[0], coords[1] + mv[1]
				if valid_coords(*newcoords) and matrix[newcoords[0]][newcoords[1]] == 1:
					q.append(newcoords)
					# mark as seen
					matrix[newcoords[0]][newcoords[1]] = 0
					size += 1
		return size
						
					
	def valid_coords(row, col):
		if 0<=row<rows and 0<=col<cols:
			return True
		else:
			return False
	
	for i in range(rows):
		for j in range(cols):
			if matrix[i][j]==1:
				size = traverse(i, j, matrix)
				res.append(size)

	return res