#O(n^2) time | O(n) space

def threeNumberSum(array, targetSum):
	array.sort()
	res = []
	
	def twosum(subarray, target):
		# assume current array is sorted
		res = []
		l, r = 0, len(subarray)-1
		while l<r:
			if subarray[l]+subarray[r]<target:
				l+=1
			elif subarray[l]+subarray[r]>target:
				r-=1
			else:
				res.append([subarray[l], subarray[r]])
				l+=1
				r-=1
		return res
	
    for i in range(len(array)-2):
		cur = array[i]
		candidates = [cur]
		for couple in twosum(array[i+1:], targetSum-cur):
			res.append([cur]+couple)
		print(res)
	return res