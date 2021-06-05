
# O(n), O(1)
# find three largest 
def findThreeLargestNumbers(array):
    # Write your code here.
    subarr = sorted(array[:3])
	for i in range(3, len(array)):
		if array[i]>=subarr[2]:
			subarr.append(array[i])
			subarr.pop(0)
		elif array[i]>=subarr[1]:
			subarr[0]=subarr[1]
			subarr[1]=array[i]
		elif array[i]>=subarr[0]:
			subarr[0]=array[i]
		else:
			continue
	return subarr


#O(n), 0(1)
#using a heap more elegant
#other soluton could be to reimplement heap or modularize above code
def findThreeLargestNumbers(array):
    # Write your code here
	import heapq
	heap = array[:3]
	for i in range(3, len(array)):
		heapq.heappush(heap, array[i])
		if len(heap)>3:
			heapq.heappop(heap)
	return sorted(heap)