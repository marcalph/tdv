# O(n+m), O(1)
# find value in sorted matrix
# find the spot that eliminates the most values
def searchInSortedMatrix(matrix, target):
    # Write your code here.
	nrows = len(matrix)
	ncols = len(matrix[0])
	
	i, j = 0, ncols-1 
	
	while i<nrows and j>=0:
		pivot = matrix[i][j]
		if target == pivot:
			return [i,j]
		elif target < pivot:
			j-=1
		else:
			i+=1
	return [-1, -1]