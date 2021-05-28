#O(2n), O(1)
def threeNumberSort(array, order):
    # Write your code here.
	from collections import Counter
	# bucket
	
	count = [0,0,0]
	for elt in array:
		count[order.index(elt)]+=1
		
	for i in range(len(order)):
		number_needed = count[i]
		value = order[i]
		for n in range(number_needed):
			idx = sum(count[:i]) + n
			array[idx] = value
		
	return array
	

#O(2n), O(1)
def threeNumberSort(array, order):
	start_unsorted, end_unsorted = 0, len(array)-1
	for moving in range(len(array)):
		if array[moving]==order[0]:
			array[start_unsorted], array[moving] = array[moving],array[start_unsorted]
			start_unsorted+=1
			
	for moving in range(len(array)-1,-1,-1):
		if array[moving]==order[2]:
			array[end_unsorted], array[moving] = array[moving],array[end_unsorted]
			end_unsorted-=1
	return array


#O(n), O(1) smart
def threeNumberSort(array, order):
	start_unsorted, moving_index, end_unsorted = 0, 0, len(array)-1
	
	while moving_index<=end_unsorted:
		if array[moving_index]==order[0]:
			array[start_unsorted], array[moving_index] = array[moving_index],array[start_unsorted]
			start_unsorted+=1
			moving_index+=1
		elif array[moving_index]==order[2]:
			array[end_unsorted], array[moving_index] = array[moving_index], array[end_unsorted]
			end_unsorted-=1
		else:
			moving_index+=1
	return array