# select kth largest/smallest 
# reuse quick sort idea
# O(n) on average, 0(1)
# O(n^2) worst case
def quickselect(array, k):
    # Write your code here.
	return partition(array, 0, len(array)-1, k-1)
	
	
	
def partition(array, start, end, k):
	while True:
		print(array)
		pivot = array[start]
		print(pivot)
		l = start+1
		r = end
		while True:
			while l<=r and pivot>=array[l]:
				l+=1
			while l<=r and pivot<=array[r]:
				r-=1
			if l<=r:
				array[l], array[r] = array[r], array[l]
			else: 
				break			
		array[start], array[r] = array[r], array[start]
		if k==r:
			return array[r]
		elif k<r:
			end=r-1
		else:
			start=r+1