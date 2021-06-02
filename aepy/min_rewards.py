# O(n^2), O(n) space
# all values are different
def minRewards(scores):
	res = [1]* len(scores)
	for i in range(1, len(scores)):
		j = i-1
		if scores[i-1]<scores[i]:
			res[i]= res[j]+1
		else: 
			while j>=0  and scores[j]>scores[j+1]:	
				res[j] = max(res[j], res[j+1]+1)
				j-=1
	print(res)
	return sum(res)


# O(n), O(n)
# find local min O(n) and expand from  left and rigth
def minRewards(scores):
	if len(scores)==1:
		return 1
	res = [1 for _ in scores]
	local_mins = get_local_mins(scores)
	print(local_mins)
	for local_min in local_mins:
		expand_from(local_min, scores, res)
	return sum(res)

		
def expand_from(local_min, scores, res):
	left = local_min - 1
	while left >= 0 and scores[left] > scores[left+1]:
		res[left] = max(res[left], res[left+1]+1)
		left -=1
	right = local_min+1
	while right<len(scores) and scores[right]>scores[right-1]:
		res[right] = res[right-1]+1
		right+=1

		
def get_local_mins(scores):
	local_mins = []
	for i in range(len(scores)):
		if is_min(i, scores):
			local_mins.append(i)
	return local_mins


def is_min(i, array):
	if i == 0:
		return array[i] < array[i+1]
	if i == len(array)-1:
		return array[i] < array[i-1]
	return array[i]<array[i+1] and array[i]<array[i-1]


# O(n), O(n)
# expand from a point can be mimicked from left to right and right to left traversal
# find local min O(n) and expand
def minRewards(scores):
	res = [1 for _ in scores]
	for i in range(1, len(scores)):
		if scores[i-1] < scores[i]:
			res[i] = res[i-1]+1
	
	for i in range(len(scores)-2, -1, -1):
		if scores[i] > scores[i+1]:
			res[i] = max(res[i], res[i+1]+1)
	
	return sum(res)


