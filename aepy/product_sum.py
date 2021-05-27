#O(n), O(d)
def productSum(array):
    # Write your code here.
	def helper(array, depth):
		cursum=0
		for i in array:
			if isinstance(i, list):
				cursum+=helper(i, depth+1)
			else:
				cursum+=i
		return cursum*depth
	
	return helper(array, 1)