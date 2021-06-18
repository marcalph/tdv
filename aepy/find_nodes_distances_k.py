
# find all nodes at distance k from target nodes
# bfs from target O(n) spacetime because of parent search
def findNodesDistanceK(tree, target, k):
    # Write your code here.
	parents = store_parents(tree, {tree.value:None})
	print(parents)
	viewed = set()
	
	targetnode = get_target(tree, target, parents)
	q = [(targetnode,0)]
	while q:
		print([tup[0].value for tup in q])
		node, dist = q.pop(0)
		if node in viewed or node is None:
			continue
					
		if dist == k:
			res =  [node.value]+[tup[0].value for tup in q]
			print(res)
			return res
		
		viewed.add(node)
		if node.left and node.left not in viewed:
			q.append((node.left, dist+1))
		if node.right and node.right not in viewed:
			q.append((node.right, dist+1))
		if parents[node.value] and parents[node.value] not in viewed:
			q.append((parents[node.value], dist+1))
		
    return []

def get_target(tree, target, parents):
	if tree.value==target:
		return tree
	parent = parents[target]
	
	if parent.left and parent.left.value==target:
		return parent.left
	return parent.right
	
def store_parents(tree, parents):
	if tree:
		if tree.left:
			parents[tree.left.value]=tree
			store_parents(tree.left, parents)
		if tree.right:
			parents[tree.right.value]=tree
			store_parents(tree.right, parents)
	return parents


#O(n) spacetime
def findNodesDistanceK(tree, target, k):
    # Write your code here.
    results = []
	find_distance_from_node_to_target(tree, target, k , results)
	return results


def find_distance_from_node_to_target(node, target, k, results):
	#target node not in branch
	if node is None:
		return -1
	
	#current node is target
	#lets look node that are k down from that nnode
	if node.value==target:
		add_nodes_k_away(node, 0, k, results)
		return 1
	
	# is node in left or right subtree
	left_dist = find_distance_from_node_to_target(node.left, target, k, results)
	right_dist = find_distance_from_node_to_target(node.right, target, k, results)

	#is current node
	if left_dist==k or right_dist==k:
		results.append(node.value)
	
	# is node in left subtree look 
	if left_dist!=-1:
		add_nodes_k_away(node.right, left_dist+1, k, results)
		return left_dist + 1
	
	if right_dist!=-1:
		add_nodes_k_away(node.left, right_dist+1, k, results)
		return right_dist + 1
	
	return -1
		
	
	
	
def add_nodes_k_away(node, depth, k, results):
	if node is None:
		return
	
	if depth==k:
		results.append(node.value)
	else:
		add_nodes_k_away(node.right, depth+1, k, results)
		add_nodes_k_away(node.left, depth+1, k , results)

