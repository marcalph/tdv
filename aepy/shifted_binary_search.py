# find target in rotated/shifted array
# binary search
# only works because shifted array

def shiftedBinarySearch(array, target):
    # Write your code here.
	l, r =0, len(array)-1
	while l<r:
		mid = (l+r)//2
		if array[mid]==target:
			return mid
		elif array[l]<=array[mid]:
			if target<array[mid] and target>=array[l]:
				r=mid
			else:
				l=mid+1
		else:
			if target>array[mid] and target<=array[r]:
				l=mid+1
			else:
				r=mid
	if array[l]==target:
		return l
	else:
		return -1