# sort array where elements are at most k away from sorted position
# O(nlog k)
# min heap
def sortKSortedArray(array, k):
    # Write your code here.
	# edge case k=0 >> array is sorted
	if k == 0:
		return array
	# else need to work
	from heapq import heapify, heappop, heappush
	min_heap = array[0:k+1]
	heapify(min_heap)
	
	next_idx = 0
	for i in range(k+1, len(array)):		
		array[next_idx] = heappop(min_heap)
		heappush(min_heap, array[i])
		next_idx += 1 
		
	while min_heap:
		array[next_idx] =heappop(min_heap)
		next_idx+=1
		
	return array
