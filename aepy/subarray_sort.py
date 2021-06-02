# O(n), O(1)
# find unordered and then unordered correct position
def subarraySort(array):
    # Write your code here.
	unordered_curmin = float("inf")
	unordered_curmax = float("-inf")
	# find unordered values
	for i in range(len(array)):
		if is_out_of_order(i, array):	
			unordered_curmin = min(unordered_curmin, array[i])
			unordered_curmax = max(unordered_curmax, array[i])
	if unordered_curmin == float("inf"): # array is sorted
		return [-1, -1]
	
	left = 0
	while array[left]<=unordered_curmin:
		left+=1

		
	right = len(array)-1	
	while array[right]>=unordered_curmax:
		right-=1
	return [left, right]


def is_out_of_order(i, array):
	if i==0:
		return array[i]>array[i+1]
	if i==len(array)-1:
		return array[i]<array[i-1]
	return array[i-1]>array[i] or array[i]> array[i+1]