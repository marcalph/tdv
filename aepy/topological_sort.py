# topological sort to find cycles?



# O(j+d) spacetime
# for both dfs and graph
# create a graph from jobs 
# start w a node, check all its prereq
def topologicalSort(jobs, deps):
    # Write your code here.
	job_graph = create_graph(jobs, deps)
	return get_ordered_jobs(job_graph)

def get_ordered_jobs(graph):
	ordered = []
	nodes = graph.nodes
	while len(nodes):
		node = nodes.pop()
		contains_cycle = dfs_traverse(node, ordered)
		if contains_cycle:
			return []
	return ordered

def dfs_traverse(node, ordered):
	if node.visited:
		return False

	if node.visiting:
		return True
	
	node.visiting = True
	for prereq in node.prereqs:
		contains_cycle = dfs_traverse(prereq, ordered)
		if contains_cycle:
			return True
	node.visited = True
	node.visiting = False
	ordered.append(node.job)
	return False
	
def create_graph(jobs, deps):
	graph = Graph(jobs)					# create graph hashmap of nodes
	for prereq, job in deps:			
		graph.add_prereq(prereq, job)	# add prereqs to the node object
    return graph


class Graph():
	def __init__(self, jobs):
		self.nodes = []
		self.graph = {}
		for job in jobs:
			self.add_node(job)
	
	def add_node(self, job):
		self.graph[job] = Node(job)
		self.nodes.append(self.graph[job])

	def add_prereq(self, prereq, job):
		job_node = self.get_node(job)
		prereq_node = self.get_node(prereq)
		job_node.prereqs.append(prereq_node)
	
	def get_node(self,job):
		return self.graph[job]
		
class Node():
	def __init__(self, job):
		self.job = job
		self.prereqs = []
		self.visited = False
		self.visiting = False