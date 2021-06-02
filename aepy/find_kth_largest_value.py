# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# brute force is inorder traversal and appending values
# then return (len - k)th value


# O(h+k), O(h)
# to solve this brain is counting from right to left
# this is reversed inorder traversal
# then it is just maintaining a counter + the last value
def findKthLargestValueInBst(tree, k):
    # Write your code here.
	nb_visited = 0
	lastnode = None
	info = [nb_visited, lastnode]
	def helper(tree, k, info):
		if  info[0]>=k:
			return
		if tree.right:
			helper(tree.right, k, info)
		if info[0]<k:
			info[0]+=1
			info[1]=tree.value
			if tree.left:
				helper(tree.left, k, info)
	helper(tree, k, info)
	return info[1]