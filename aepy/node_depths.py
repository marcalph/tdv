# O(n) time | O(h) space
#sums of nodes depths/heights
def nodeDepths(root):
	sumOfDepths = 0
	stack = [{"node": root, "depth": 0}]
	while len(stack) > 0:
		nodeInfo = stack.pop()
		node, depth = nodeInfo["node"], nodeInfo["depth
		if node is None:
			continue
		sumOfDepths += depth
		stack.append({"node": node.left, "depth": depth+1})
		stack.append({"node":node.right, 'depth':depth+1})
	return sumOfDepths

# O(n) time | O(h space)
def nodeDepths(root):
    # Write your code here.
	sum_ = 0
	def helper(node, depth):
		if node is None:
			return 0
		return depth + helper(node.left, depth+1) + helper(node.right, depth+1)
		
	return helper(root,0)