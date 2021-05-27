
# O(n)time, O(1)space
# find the longest peak in array
def longestPeak(array):
    # Write your code here.
	peaks = []
	longestlen =0
    for i in range(1, len(array)-1):
		if array[i-1]<array[i] and array[i]>array[i+1]:
			left = i-2
			right = i+2
			while left>=0 and array[left]<array[left+1]:
				left-=1
			while right<len(array) and array[right-1]>array[right]:
				right+=1
			longestlen = max(longestlen, right-left-1)
			i=right
		else:
			continue
	return longestlen