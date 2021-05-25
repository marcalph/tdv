# O(n) | O(h)
class Info():
	def __init__(self, diam, height):
		self.diam = diam
		self.height = height
		
def binaryTreeDiameter(tree):
	return helper(tree).diam

def helper(node):
	if node is None:
		return Info(0, 0)
	leftinfo = helper(node.left)
	rightinfo = helper(node.right)
	
	cur_longestpaththroughnode = leftinfo.height + rightinfo.height
	cur_maxdiam = max(leftinfo.diam, rightinfo.diam)
	diam = max(cur_longestpaththroughnode, cur_maxdiam)
	height = 1+max(leftinfo.height, rightinfo.height)
	
	return Info(diam, height)