#max path sum in binary tree

def maxPathSum(tree):
    # Write your code here.
	
	from collections import namedtuple
	nodeinfo = namedtuple("nodeinfo", "value, branch, max")
	
	def helper_traverse(node):
		# base case
		if node is None:
			return nodeinfo(node, float("-inf"), float("-inf"))
		# reccurrence
		leftinfo = helper_traverse(node.left)
		rightinfo = helper_traverse(node.right)
		
		# logic
		branchpathsum = max(leftinfo.branch+node.value, rightinfo.branch+node.value, node.value)
		maxasroot = max(node.value+leftinfo.branch+rightinfo.branch, branchpathsum)
		res = nodeinfo(node.value, branchpathsum, max(leftinfo.max, rightinfo.max, maxasroot))
		return res
	
	
	return helper_traverse(tree).max
