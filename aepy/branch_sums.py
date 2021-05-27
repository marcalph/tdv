# O(n) spacetime
def branchSums(root):
    # Write your code here.
    res = []
	cursum = 0
	if root is None:
		return cursum
		
	def helper(node, cursum):
		if node.left is None and node.right is None: # leaf
			res.append(cursum+node.value)
		if node.left:
			helper(node.left, cursum+node.value)
		if node.right:
			helper(node.right, cursum+node.value)
	
	helper(root, cursum)
	return res