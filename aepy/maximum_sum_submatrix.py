# O(wh) spacetime
# brute force is O(wh*size^2)
# need to precompute sums smartly so that we only need to traverse matrix O(wh)
# and the sum is computed in constant time
def maximumSumSubmatrix(matrix, size):
	sums = createSumMatrix(matrix)
	print(sums)
	maxSubMatrixSum = float("-inf")
	for row in range(size - 1, len(matrix)):
		for col in range(size - 1, len(matrix[row])):
			total = sums[row][col]
	
			touchesTopBorder = row - size < 0
			if not touchesTopBorder:
				total -= sums[row - size][col]

			touchesLeftBorder = col - size < 0
			if not touchesLeftBorder:
				total -= sums[row][col - size]

			touchesTopOrLeftBorder = touchesTopBorder or touchesLeftBorder
			if not touchesTopOrLeftBorder:
				total += sums[row - size][col - size]
		
			maxSubMatrixSum = max(maxSubMatrixSum, total)
	
	return maxSubMatrixSum

def createSumMatrix(matrix):
	sums = [[0 for __ in range(len(matrix[row]))] for row in range(len(matrix))]
	sums[0][0] = matrix[0][0]
	
	# Fill the first row.
	for idx in range(1, len(matrix[0])):
		sums[0][idx] = sums[0][idx - 1] + matrix[0][idx]
		
	# Fill the first column.
	for idx in range(1, len(matrix)):
		sums[idx][0] = sums[idx - 1][0] + matrix[idx][0]
		
	# Fill the rest of the matrix.
	for row in range(1, len(matrix)):
		for col in range(1, len(matrix[row])):
			sums[row][col] = sums[row - 1][col] + sums[row][col - 1] - sums[row-1][col-1]+matrix[row][col]
	
	return sums