
# recursive
# O(h) spacetime
def findClosestValueInBst(tree, target):
    # Write your code here.
	return helper(tree, target, tree.value)

def helper(tree, target, closest):
    if tree==None:
		return closest
	if abs(target-closest)>abs(target-tree.value):
		closest = tree.value
	if tree.value>target:
		return helper(tree.left, target, closest)
	elif tree.value<target:	
		return helper(tree.right, target, closest)
	else:
		return closest


#iterative
#O(h), O(1)
def findClosestValueInBst(tree, target):
	closest = float("inf")
	curNode = tree
	while curNode is not None:
		if abs(target-curNode.value)<abs(target-closest):
			closest = curNode.value
		if target<curNode.value:
			curNode = curNode.left
		else:
			curNode = curNode.right
	return closest