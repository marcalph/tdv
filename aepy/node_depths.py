

# O(n) time | O(h space)
def nodeDepths(root):
    # Write your code here.
	sum_ = 0
	def helper(node, depth):
		if node is None:
			return 0
		return depth + helper(node.left, depth+1) + helper(node.right, depth+1)
		
	return helper(root,0)