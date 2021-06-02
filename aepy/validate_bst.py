# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#O(n), O(d) recursive
def validateBst(tree):
    # Write your code here.
    def helper(node, minval, maxval):
		if node is None:
			return True
		if node.value<minval or node.value>=maxval:
			return False
    	return helper(node.left, minval, node.value) and helper(node.right, node.value, maxval)
	return helper(tree, float("-inf"), float("inf"))

#O(n), O(d) iterative
def validateBst(tree):
    # Write your code here.
    from collections import namedtuple
	nodeinfo = namedtuple("info", "node, nodeval, lower, upper")
	stack = [nodeinfo(tree, tree.value, float("-inf"), float("inf"))]
	while stack:
		current = stack.pop()
		print(current)
		node, lowerbound, upperbound = current.node, current.lower, current.upper
		if not lowerbound<=node.value<upperbound:
			print("broken node", node.value)
			return False
		if node.left:
			stack.append(nodeinfo(node.left, node.value, lowerbound, node.value))
		if node.right:
			stack.append(nodeinfo(node.right,node.value, node.value, upperbound))
	return True