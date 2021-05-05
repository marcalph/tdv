#O(n^2) time | O(1)space

def selectionSort(array):
    # Write your code here.
    for i in range(len(array)):
		idxmin=i
		for j in range(i+1, len(array)):
			if array[j]<array[idxmin]:
				idxmin=j
		array[i], array[idxmin] = array[idxmin], array[i]
	return array
