# O(n) time , O(h)
class Info():
	def __init__(self, height, balanced):
		self.height = height
		self.balanced = balanced

#O(n), O(h)
# need to propagate height and balanced info upwards
def heightBalancedBinaryTree(tree):
    # Write your code here.
	from collections import namedtuple
	tree_info = namedtuple("tree_info", "height, response")
	
	def helper_traverse(node):
		# base case
		if node is None:
			return tree_info(0, True)
		# recursion
		left_info = helper_traverse(node.left)
		right_info = helper_traverse(node.right)
		
		response = left_info.response and right_info.response and abs(left_info.height-right_info.height)<=1

		height = 1+max(left_info.height, right_info.height)
		return tree_info(height, response)
	
	return helper_traverse(tree).response