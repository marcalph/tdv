
# O(n) spacetime w/o sort
#loops in opposite direction
def sunsetViews_(buildings, direction):
    # Write your code here.
	res = []
	# keep track of running max
	curmax = 0 	
	if direction == "EAST":
		for i in range(len(buildings)-1, -1, -1):
			if buildings[i]>curmax:
				res.append(i)
				curmax=buildings[i]
		return res[::-1]
	else:
		for i in range(len(buildings)):
			if buildings[i]>curmax:
				res.append(i)
				curmax=buildings[i]
	return res

#another smart solution O(2n) w/sort with stack (loop is in the same direction )
def sunsetViews(buildings, direction):
	stack = []
	start = 0 if direction=="EAST" else len(buildings)-1
	step = +1 if direction == "EAST" else -1
	
	idx = start
	while 0<=idx<len(buildings):
		curheight = buildings[idx]
		
		while len(stack) > 0 and curheight >= buildings[stack[-1]]:
			stack.pop()
			
		stack.append(idx)		
		idx+=step
		
	if direction == "WEST":
		return stack[::-1]
	return stack