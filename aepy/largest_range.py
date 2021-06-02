# O(n) spacetime
# find largest range in present in array
# obvious is sorting, but linear solution use hashmap for fast access
# and expands ranges on the fly
def largestRange(array):
    # Write your code here.
    viewed = {}
	for num in array:
		viewed[num] = False
	
	best = [0, 0]
	for i in range(len(array)):
		num = array[i]
		if num in viewed:
			best = expand_from(viewed, num, best)
	
	return best

			
def expand_from(viewed, num, best):
	if not viewed[num]:
		viewed[num] = True
		left, right = num-1, num+1
		while left in viewed:
			viewed[left]=True
			left-=1
		
		while right in viewed:
			viewed[right]=True
			right+=1
	
		if right-left-1 >= best[1]-best[0]+1:
			best = [left+1, right-1]
	return best