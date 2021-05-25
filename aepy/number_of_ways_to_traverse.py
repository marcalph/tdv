# O(2^(n+m)) , O(n+m) for traversal
# O(n*m) spacetime for dp
# O(n+m) for combinatorics
def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.
    class Info():
		def __init__(self, count):
			self.count=count

	info = Info(0)
	def recursive_dfs(row, col, count):
		# base case
		if row>=height or col>=width:
			return None
		if row==height-1 and col==width-1:
			info.count+=1
			return None
		recursive_dfs(row+1, col, info)
		recursive_dfs(row, col+1, info)
	
	def iterative_dfs(row, col, info):
		stack = []
		stack.append((row, col))
		while stack:
			r,c = stack.pop()
			if r>=height or c >= width:
				continue
			if r==height-1 and c==width-1:
				info.count+=1
			stack.append((r+1,c))
			stack.append((r, c+1))
    
    def iterative_bfs(row, col, info):
		q = []
		q.append((row,col))
		while q:
			r,c = q.pop(0)
			if r>=height or c >= width:
				continue
			if r==height-1 and c==width-1:
				info.count+=1
			q.append((r+1, c))
			q.append((r, c+1))

    q = []
	q.append((0, 0))
	def recursive_bfs(q, info):
		if not q:
			return
		r,c = q.pop(0)
		if r>=height or c >= width:
			return
		if r==height-1 and c==width-1:
			info.count+=1
		q.append((r+1, c))
		q.append((r, c+1))
		recursive_bfs(q, info)
		recursive_bfs(q, info)
		