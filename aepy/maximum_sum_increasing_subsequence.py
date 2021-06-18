# find max sum with strictly increasing subsequence
# dp with rebuilding
#O(n^2), O(n)

def maxSumIncreasingSubsequence(array):
    # Write your code here.
	sums = array[:]
	curmax = float("-inf")
	curmax_idx = None
	seq = [None] * len(array)
	
	# construct dp array of max sums given constraints
	for i in range(len(array)):
		rsum = 0
		cur = array[i]
		maxidx=i
		for j in range(0, i):
			prev = array[j]
			if prev<cur and sums[j]+cur>=sums[i]:
				sums[i]=sums[j]+cur
				seq[i] = j
		if sums[i]>curmax:
			curmax = sums[i]
			curmax_idx = i
	
	# rebuild sequence
	i = curmax_idx
	res = []
	while i is not None:
		res.append(array[i])
		i = seq[i]
		
	print(sums)
	print(seq)
	print(res)
	return [curmax, res[::-1]]	