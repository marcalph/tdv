
#O(nlogn ) time | O(n) space
def mergeOverlappingIntervals(intervals):
    # Write your code here.
	print(intervals)
	intervals.sort(key=lambda tup: tup[0])
	i=0
	if len(intervals)<=1:
		return intervals
	while i <len(intervals)-1:
		i1 = intervals[i]
		i2 = intervals[i+1]
		if i1[1]>=i2[0]:
			sup = max(i1[1], i2[1])
			inf = min(i1[0], i2[0])
			intervals[i]=[inf, sup]
			del intervals[i+1]
		else:
			i+=1
		print(intervals)
    return intervals