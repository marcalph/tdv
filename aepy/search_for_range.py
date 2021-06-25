# find range of indices for target in array
# binary search
# one for finding leftmost index, one for rightmost
# test for value at loop exit

def searchForRange(array, target):
    # Write your code here.
    l  = bsleft(array, target, 0, len(array)-1)
	if l==-1:
		return [-1, -1]
	else:
		r = bsright(array, target, l, len(array)-1)
	return [l, r]



def bsleft(array, target, l, r):
	while l<r:
		mid = (l+r )//2
		if array[mid]<target:
			l=mid+1
		else:
			r=mid
	if array[l]==target:
		return l
	else:
		return -1

	
def bsright(array, target, l, r):
	while l<r:
		mid = (l+r )//2
		if array[mid]<=target:
			l=mid+1
		else:
			r=mid
	if array[l]==target:
		return l
	else:
		return l-1