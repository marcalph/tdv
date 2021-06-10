# O(n log n), O(log n) 
# big O space if coded optimally with recursive call on smaller subarray and tail recursion

def quickSort(array):
    # Write your code here.
	qs(array, 0, len(array)-1)
	return array
    

def qs(arr, start, end):
	if start>= end:
		return
	p = partition(arr, start, end)
	if p-start-1<end-p-1:
		qs(arr, start, p-1)
		qs(arr, p+1, end)
	else:
		qs(arr, p+1, end)
		qs(arr, start, p-1)
	
	
def partition(arr, start, end):
	pivot = arr[start]
	l = start+1
	r = end
	while True:
		while l<=r and arr[l] <= pivot:
			l+=1
		while l<=r and pivot <= arr[r]:
			r-=1
		if l<=r:
			arr[r], arr[l] = arr[l], arr[r]
		else:
			break
	arr[r], arr[start] = arr[start], arr[r]
	return r