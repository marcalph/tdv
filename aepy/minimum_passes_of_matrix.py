# O(nm) spacetime
# determine how many passes needed to convert whole matrix to positiv (if possible)
# find pos values andd add them to queue/stack
# switch neighbors to postiive and add them to second queue/stack
# all could be done with single queue! (not stack)
#make code more modular!!! (more functions)
def minimumPassesOfMatrix(matrix):
    # Write your code here.
	n = len(matrix)
	m = len(matrix[0])
	q0 = []
	q1 = []
	for i in range(n):
		for j in range(m):
			if matrix[i][j]>0:
				q0.append((i,j))
	
	npass = 0
	while q0:
		i, j = q0.pop()
		for nei in get_neighbors(i, j, matrix):
			x, y = nei
			if matrix[x][y]<0:
				matrix[x][y] *= -1
				q1.append(nei)
		if len(q0)==0:
			q0 = q1
			q1 = []
			npass+=1
	
	for i in range(n):
		for j in range(m):
			if matrix[i][j]<0:
				return -1
	return npass-1


def is_valid(i, j, matrix):
	n = len(matrix)
	m = len(matrix[0])
	return 0<=i<n and 0<=j<m


def get_neighbors(i, j, matrix):
	moves = [
		(0, +1),  # right
		(0, -1),
		(+1, 0),
		(-1, 0)
	]
	neighbors = []
	for mv in moves:
		newi, newj = i+mv[0], j+mv[1]
		if is_valid(newi, newj, matrix):
			neighbors.append((newi, newj))
	return neighbors