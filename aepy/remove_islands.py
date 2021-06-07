# O(wd) spacetime
# remove islands if not connected to border
# store island
def removeIslands(matrix):
    # "your code here."
	nrows = len(matrix)
	ncols = len(matrix[0])
	
	moves = [
		(-1, 0), # up	
		(+1, 0), # down
		(0, -1), # left
		(0, +1), # right
	]
	
    # mark border/nonvalid islands
	for i in range(nrows):
		for j in range(ncols):
			if is_border(i, j, matrix) and matrix[i][j]==1:
				#todo better
				traverse(i, j, matrix, moves)
			else:
				continue
	
	for i in range(nrows):
		for j in range(ncols):
			if matrix[i][j] == 2:
				matrix[i][j] = 1
			elif matrix[i][j] == 1:
				matrix[i][j] = 0
			else:
				continue
	return matrix
	




def traverse(row, col, matrix, moves):
	# "bfs" traversal for "1"s
	q = [] 
	q.append((row,col))
	matrix[row][col] = 2
	while q: # is not empty
		coords = q.pop(0)
		for mv in moves:
			# expand search
			newcoords = coords[0] + mv[0], coords[1] + mv[1]
			if is_valid(*newcoords, matrix) and matrix[newcoords[0]][newcoords[1]]==1:
				q.append(newcoords)
				matrix[newcoords[0]][newcoords[1]] = 2
			else:
				continue
		


def is_valid(row, col, matrix):
	if 0<=row<len(matrix) and 0<=col<len(matrix[0]):
		return True
	return False


def is_border(row, col, matrix):
	if row==0 or col==0 or row==len(matrix)-1 or col==len(matrix[0])-1:
		return True
	return False