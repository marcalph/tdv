# O(n^3)>> O(n^2) on average, O(n^2)
# two pairs
# other solution recursive + twosum
def fourNumberSum(array, targetSum):
	pair_sums = {}
	res = []
	for i in range(1, len(array)-1):
		for j in range(i+1, len(array)):
			current = array[i]+array[j]
			diff = targetSum-current
			if diff in pair_sums:
				for pair in pair_sums[diff]:
					res.append(pair+[array[i], array[j]])
		print(res)
		for k in range(0,i):
			current = array[i]+array[k]
			if current not in pair_sums:
				pair_sums[current] = [[array[k], array[i]]]
			else:
				pair_sums[current].append([array[k], array[i]])
		print(pair_sums)
	return res