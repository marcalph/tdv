# O(n) time , O(h)
class Info():
	def __init__(self, height, balanced):
		self.height = height
		self.balanced = balanced

def heightBalancedBinaryTree(tree):
    # Write your code here.
	def helper(node):
		if node is None:
			return Info(-1, True)
		
		left = helper(node.left)
		right = helper(node.right)
		
		balanced = left.balanced==True and right.balanced==True and  abs(left.height-right.height)<=1
		if balanced:
			return Info(max(left.height, right.height)+1, True)
		else:
			return Info(max(left.height, right.height)+1, False)
		
    return helper(tree).balanced