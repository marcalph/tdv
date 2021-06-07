

# O(nlogn) , O(n)
# construct pairs of tasks such that max sum is smallest
# greedy w/ a ds to keep indices beff=ore
def taskAssignment(k, tasks):
    # minimize time by grouping task
	from collections import defaultdict
	indices = defaultdict(list)
	for i, v in enumerate(tasks):
		indices[v].append(i)
		
	res=[]
	tasks.sort()
	print(tasks)
	for _ in range(k):
		start = tasks.pop(0)
		end = tasks.pop()
		res.append([indices[start].pop(), indices[end].pop()])
	return res
