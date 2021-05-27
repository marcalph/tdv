#O(n^2), O(1)
#bubble largest element at the end of array 
def bubbleSort(array):
    # Write your code here.
    end = len(array)-1
	while end!=0:
		for i in range(end):
			if array[i]>array[i+1]:
				array[i], array[i+1] = array[i+1], array[i]
		end-=1
	print(array)
	return array