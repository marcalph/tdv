# O(n) | O(h)
# use info to propagate current state (could be namedtuple also)
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




from collections import namedtuple
info = namedtuple("info", "diam, height, depth, val")
def helper(node, depth):
	if node is None:
		return info(0, 0, depth+1, node)

	leftinfo = helper(node.left, depth+1)
	rightinfo = helper(node.right, depth+1)
	
	cur_longestpaththroughnode = leftinfo.height + rightinfo.height
	cur_maxdiam = max(leftinfo.diam, rightinfo.diam)
	diam = max(cur_longestpaththroughnode, cur_maxdiam)
	height = 1+max(leftinfo.height, rightinfo.height)
	
	return info(diam, height, depth, node.value)