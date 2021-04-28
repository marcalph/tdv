
#O(n) spacetime
def sortedSquaredArray(array):
    # Write your code here.
	l,r = 0, len(array)-1
	res =[]
	while len(res)<len(array):
		if abs(array[l])>abs(array[r]):
			res.append(array[l]**2)
			l+=1
		else:
			res.append(array[r]**2)
			r-=1
	return res[::-1]