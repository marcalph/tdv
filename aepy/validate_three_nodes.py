# check if node2 between node1 and node3 in a BST
# dfs O(h), O(1)
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    # Write your code here.
	if check_descendant(nodeOne, nodeTwo):
		return check_descendant(nodeTwo, nodeThree)
	if check_descendant(nodeThree, nodeTwo):
		return check_descendant(nodeTwo, nodeOne)
	
    return False

def check_descendant(parent, child):
	current = parent
	while current and current is not child:
		if child.value<current.value:
			current = current.left
		else:
			current = current.right
	return current is child



# could land a better solution iwith early stopping
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    # Write your code here.
    found3from1, found2from1 = check_descendant(nodeTwo, nodeOne, nodeThree)
    found1from3, found2from3 = check_descendant(nodeTwo, nodeThree, nodeOne)
	if found1from3 or found1from3:
		return False
	if found2from1:
		return check_descendant(nodeThree, nodeTwo, None)[1]
	if found2from3:
		return check_descendant(nodeOne, nodeTwo, None)[1]
	return False


def check_descendant(child, parent, other):
	current = parent
	while current and current is not child:
		if current is other:
			return True, False
		if child.value<current.value:
			current = current.left
		else:
			current = current.right
	return False, current is child