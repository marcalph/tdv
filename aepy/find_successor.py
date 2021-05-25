#O(n) spacetime

def getleftmost(node):
	"""	return leftmost or None
	"""
	cur = node
	while cur.left:
		cur = cur.left
	return cur


def getrightmostparent(node):
	cur = node
	while cur.parent  and cur.parent.right==cur:
		cur = cur.parent
	return cur.parent


def findSuccessor(tree, node):
    # Write your code here.
	if node.right :
		return getleftmost(node.right) 
	
	return getrightmostparent(node)
		
		