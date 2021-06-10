# O(n) spacetime
# find out which is the next greater element in the array (in a circular way)
# use a stack to store indices if element at index is bigger 
# could be done by traversing in reverse order

def nextGreaterElement(array):
    # Write your code here.
    s = []
	res = [-1]* len(array)
	for i in range(2*len(array)):
		idx = i%len(array)
		while s and array[s[-1]]<array[idx]:
			res[s.pop()]=array[idx]
		s.append(idx)
			
		
	return res
