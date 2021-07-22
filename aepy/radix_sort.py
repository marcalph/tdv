def radixSort(array):
    # Write your code here.
	if not len(array):
		return []
    max_digits = len(str(max(array)))
	for i in range(max_digits):
		array = counting_sort(array, i)
	return array



def counting_sort(array, digit, base=10):
	counts = [0]*base
	sorted_res = [0]*len(array)
	# count by digit
	for num in array:
		current = num//10**digit%base
		counts[current]+=1
	print("initial counts", counts)
	
	# find last position by digit
	for i in range(1, base):
		counts[i]+=counts[i-1]
	print("last pos", counts)
	
	# construct res
	for num in array[::-1]:
		current = int(str(num)[-digit-1]) if digit<len(str(num)) else 0 # alternative to num//10**digit%base
		counts[current]-=1
		sorted_res[counts[current]]=num
	return sorted_res