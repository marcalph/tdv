# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(h+k) time, h height, k kth rank
# O(h) space for the call stack
def findKthLargestValueInBst(tree, k):
    # Write your code here.
	visited = 0
	lastnode = None
	info = [visited, lastnode]
	def helper(tree, k, info):
		if tree is None or info[0]>=k:
			return
		helper(tree.right, k, info)
		if info[0]<k:
			info[0]+=1
			info[1]=tree.value
			helper(tree.left, k, info)
	helper(tree, k, info)
	return info[1]