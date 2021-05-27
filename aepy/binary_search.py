#O(log n) spacetime
def binarySearch(array, target):
    # Write your code here.
    l, r = 0, len(array)-1
	while l<=r:
		mid = (l+r)//2
		if array[mid]>target:
			print("move r")
			r = mid-1
		elif array[mid]<target:
			print("move l")
			l = mid+1
		else: 
			return mid
	return -1