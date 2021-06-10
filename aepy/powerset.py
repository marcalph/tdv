
# O(n 2^n) spacetime
# iterative
# start with empty than append evry elt of array
# []>>[],[1]>> [],[2],[1][1,2]>>...
def powerset(array):
    # Write your code here.
	res = []
	res.append([])
	for elt in array:
		for i in range(len(res)):
			res.append(res[i]+[elt])
	return res

# recursive
def powerset(array):
	res = []
		
	def helper(res, array, i=len(array)-1):
		print("helper called with i =", i)
		if i ==-1:
			return [[]]
		
		res = helper(res, array, i-1)
		for j in range(len(res)):
			res.append(res[j]+[array[i]])
		return res
	
	res = helper(res, array)
	return res
		