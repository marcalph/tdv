
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