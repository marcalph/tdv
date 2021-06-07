#O(v+e), O(v)
def cycleInGraph(edges):
    # Write your code here.
	unvisited, visiting, visited = 0, 1, 2
	number_of_nodes = len(edges)
	state = [unvisited] * number_of_nodes
	
	def find_cycle(node, state, edges):
		state[node] = visiting

		neighbors = edges[node]
		for nei in neighbors:
			if state[nei]==visiting:
				return True
			elif state[nei]==visited:
				continue
			
			cycle = find_cycle(nei, state, edges)
			if cycle:
				return True
		state[node] = visited
		
		
	
	for node in range(number_of_nodes):
		if state[node]==unvisited:
			if find_cycle(node, state, edges):
				return True
	return False


def cycleInGraph(edges):
    # Write your code here.
	def traverse(node, visited, visiting):	
		visited.add(node)
		visiting.add(node)
		for child in edges[node]:
			if child in visiting:
				return True
			if traverse(child, visited, visiting):
				return True
		
		visiting.remove(node)
		return False
	
	visited = set()
	visiting = set()
	for node in range(len(edges)):
		if node in visited:
			continue
			
		if traverse(node, visited, visiting):
			return True
    return False