
#O(n) time, O(1) space
# find duplicate value in specific range
# either set or modify values inplace to mark as seen
def firstDuplicateValue(array):
    # Write your code here.
	
	for i in range(len(array)):
    	idx = abs(array[i])-1
		if array[idx]<0:
			return abs(array[i])
		array[idx]*=-1
	return -1
