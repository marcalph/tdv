# O(v^2+e), O(v)
# using an array
# finding closests paths from given node
# for every node
#    go to the closest node, >> min 
#    mark that node as visited
#    check all the children from that node
#    update shortest path
def dijkstrasAlgorithm(start, edges):
    # Write your code here.
	nodes_number = len(edges)
	
	min_distances = [float("inf") for _ in range(nodes_number)]
	min_distances[start] = 0
	
	visited = set()

	while len(visited) != nodes_number:
		node, current_min_distance = get_node_with_min_distance(min_distances, visited) # select closest node, takes O(nodes)
		
		if current_min_distance == float("inf"): # >> there no way to get to that node
			break
		
		visited.add(node)
		
		for edge in edges[node]: # check all edges from that node to see if there is a shorter path
			destination, distance_to_node = edge
			
			if destination in visited:
				continue
			
			new_path = current_min_distance + distance_to_node
			current_path = min_distances[destination]
			if new_path < current_path:
				min_distances[destination] = new_path
				
	return list(map(lambda x : -1 if x==float("inf") else x, min_distances))

	
def get_node_with_min_distance(min_distances, visited):
	cur_min_distance =float("inf")
	node = None
	
	for node_idx, distance in enumerate(min_distances):
		if node_idx in  visited:
			continue
		
		if distance <= cur_min_distance:
			node = node_idx
			cur_min_distance = distance
		
	return node, cur_min_distance
	
	