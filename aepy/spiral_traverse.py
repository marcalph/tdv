
#O(n)spacetime
def spiralTraverse(array):
    # Write your code here.
    n = len(array)-1
	if n==0:
		return array[0] 
	m = len(array[0])-1
	res = []
	def helper(rowstart, rowend, colstart, colend):
		if rowstart<=rowend and colstart<=colend:
			for i in range(colstart, colend+1):
				res.append(array[rowstart][i])
			print(res)
			for i in range(rowstart+1, rowend+1):
                res.append(array[i][colend])
			print(res)
			for i in reversed(range(colstart, colend)):
				if rowstart==rowend:
					break
                res.append(array[rowend][i])
			print(res)
			for i in reversed(range(rowstart+1, rowend)):
				if colstart==colend:
					break
                res.append(array[i][colstart])
			print(res)
			helper(rowstart+1,rowend-1, colstart+1, colend-1)
		else:
			return
	helper(0, n, 0, m)
	return res