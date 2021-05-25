#O(n), O(1)
def kadanesAlgorithm(array):
    # Write your code here.
    cursum = float("-inf")				# current sum
	curmax = float("-inf")  # current max
	for num in array:
		cursum = max(cursum+num, num)
		curmax = max(cursum, curmax)
	return curmax