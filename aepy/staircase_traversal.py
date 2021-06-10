# recursive  w/ memoization
# O(k*n) , O(n) n stairs, k maxstep
# best is iterative (dp) + sliding window!!!!
def staircaseTraversal(height, maxSteps):
    # Write your code here.
    moves = list(range(1, maxSteps+1))
	mem={}
	def helper(curheight, mem):
		# base case
		if curheight>height:
			return 0
		if curheight == height:
			return 1
		if curheight in mem:
			return mem[curheight]
		else:
			nways=0
			for m in moves:
				nways += helper(curheight+m, mem)
			mem[curheight] = nways
		return mem[curheight]
    nways = helper(0, mem)
	print(mem)
	return nways

