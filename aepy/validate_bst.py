# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    # Write your code here.
    def helper(node, minval, maxval):
		if node is None:
			return True
		if node.value<minval or node.value>=maxval:
			return False
    	return helper(node.left, minval, node.value) and helper(node.right, node.value, maxval)
	return helper(tree, float("-inf"), float("inf"))
