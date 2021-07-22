# find smallest index such that idx==array[idx] in a sorted array
# brute force is linear scan
# binary search
# O(logn) O(1)

def indexEqualsValue(array):
    # Write your code here.
	if len(array)==0:
		return -1
	def condition(idx):
		return idx<=array[idx]
	print(array)
	l,r =0, len(array)-1
	while l<r:
		mid = l+r>>1
		print(mid)
		if condition(mid):
			r=mid
		else:
			l=mid+1
			
    if l==array[l]:
		return l
	else:
		return -1
