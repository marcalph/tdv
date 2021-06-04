# find the minnim number of jump to go from index 0 to n-1
# dp
# O(n^2), O(n)
def minNumberOfJumps(array):
    # Write your code here.
	njumps = [float("inf") for _ in array]
	njumps[0] = 0
	for i in range(1, len(array)):
		for j in range(i):
			if array[j]+j>=i:
				njumps[i] = min(njumps[j]+1, njumps[i])
	
    return njumps[-1]


# O(n), O(1)
#smart using reach and steps to get there
def minNumberOfJumps(array):
	maxreach = array[0]
	steps = maxreach
	jumps = 0
	
	if len(array)<=1:
		return 0
	
	for i in range(1, len(array)-1): 
		print(i)
		maxreach = max(maxreach, i+array[i])
		steps -= 1
		if steps == 0:
			jumps+=1
			steps= maxreach-i
			
	return jumps+1