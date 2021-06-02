
#O(n), O(d)
def invertBinaryTree(tree):
    # Write your code here.
	if tree is None:
		return None
	
    tree.left, tree.right = tree.right, tree.left
	invertBinaryTree(tree.left)
	invertBinaryTree(tree.right)

def invertBinaryTree(tree):
    # Write your code here.
	stack = [tree]
	while stack:
		node = stack.pop()
		if node is None:
			continue
		stack.append(node.right)
		stack.append(node.left)
		node.right, node.left = node.left, node.right
		
	return tree
	