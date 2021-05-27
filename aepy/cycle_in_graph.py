#O(v+e), O(v)
def cycleInGraph(edges):
    # Write your code here.
	unvisited, opened, closed = 0,1,2
    state = [unvisited] * len(edges)
	seen = set()
	def helper(node, state):
		# dfs
		state[node] = opened
		
		neighbors = edges[node]
		for nei in neighbors:
			if state[nei]==opened:
				return True
			
			if state[nei]==closed:
				continue
				
			if state[nei]==unvisited and helper(nei, state):
				return True
			
		state[node]=closed
		return False
	
	
	for node in range(len(edges)):
		if state[node]!=unvisited:
			continue
		
		if helper(node, state):
			return True
	return False