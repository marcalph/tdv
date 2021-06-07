# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

#O(n^2) | O(h) call stack+ O(n) for the BST
# reconstruct bst from preorder
# root is current val, left is next, right is next greater
def reconstructBst(preOrderTraversalValues):
    # Write your code here.
	if len(preOrderTraversalValues)==0:
		return None
	
	current_value = preOrderTraversalValues[0]
	right_subtree_idx = len(preOrderTraversalValues)
	
	for idx in range(1, len(preOrderTraversalValues)):
        value = preOrderTraversalValues[idx]
		if value >= current_value:
			right_subtree_idx = idx
			break
	print(right_subtree_idx)
	left = reconstructBst(preOrderTraversalValues[1:right_subtree_idx])
	right = reconstructBst(preOrderTraversalValues[right_subtree_idx:])
	return BST(current_value, left, right)








#O(n) time, O(h) callstack + O(n) for the response
# use uppper and lower bounds of bst node
class treeinfo:
	def __init__(self, root_idx):
		self.root_idx = root_idx
		

def reconstructBst(preOrderTraversalValues):
    # Write your code here.
	treein = treeinfo(0)
	return helper(float("-inf"), float("inf"), preOrderTraversalValues, treein)
	

def helper(inf, sup, preOrderTraversalValues, currentsubtreeinfo):
	if currentsubtreeinfo.root_idx == len(preOrderTraversalValues):
		return None

	root_value = preOrderTraversalValues[currentsubtreeinfo.root_idx]
	if root_value < inf or root_value>=sup:
		return None

	currentsubtreeinfo.root_idx+=1
	left = helper(inf, root_value, preOrderTraversalValues, currentsubtreeinfo)
	right = helper(root_value, sup, preOrderTraversalValues, currentsubtreeinfo)
	return BST(root_value, left, right)
	