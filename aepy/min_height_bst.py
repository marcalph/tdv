# O(nlogn) time | O(n) space
def minHeightBst(array):
	
	def helper(bst, start_idx, end_idx):
		if start_idx>end_idx:
			return None
		mid = (start_idx + end_idx)//2
		value_to_add = array[mid]
		if bst is None:
			bst = BST(value_to_add)
		else:
			bst.insert(value_to_add)
		helper(bst, start_idx, mid-1)
		helper(bst, mid+1, end_idx)
		return bst
	
	bst = helper(None, 0, len(array)-1)
	return bst


# O(n) spacetime
def minHeightBst(array):
	def helper(start_idx, end_idx):
		if start_idx>end_idx:
			return None
		mid = (start_idx + end_idx)//2
		value_to_add = array[mid]
		bst = BST(value_to_add)
		bst.left = helper(start_idx, mid-1)
		bst.right = helper(mid+1, end_idx)
		return bst
	
	bst = helper(0, len(array)-1)
	return bst