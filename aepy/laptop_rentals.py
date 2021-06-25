# find minimum number of laptop needed by counting max overlapping intervals
# O(n log n), O(n)
# with either start and end times(both sorted) + double pointer
# or min heap  of end times + times sprted by start

# third solution in O(range start times + n) spacetime
def laptopRentals(times):
    # Write your code here.
	starts = sorted([t[0] for t in times])
	ends = sorted([t[1] for t in times])
	
	used=0
	curmax = 0
	s_idx, end_idx = 0, 0 
	while s_idx <len(times):
		if starts[s_idx]>=ends[end_idx]:
			used-=1
			end_idx+=1
		used+=1
		s_idx+=1
		curmax = max(used, curmax)
		
    return used


def laptopRentals(times):
    # Write your code here.
	from heapq import heappush, heappop
	if not times:
		return 0
	times.sort(key=lambda d: d[0])
	min_heap = [times[0][1]]
	for s, e in times[1:]:
		if min_heap[0]>s:
			heappush(min_heap, e)
		else:
			heappop(min_heap)
			heappush(min_heap, e)
	return len(min_heap)


#third
def laptopRentals(times):
    # Write your code here.
	if not times:
		return 0
	minstart, maxstart = get_min_max_start(times)
	print(minstart, maxstart)
	variations = [0] * (maxstart-minstart+1)
	print(variations)
	for s, e in times:
		variations[s-minstart]+=1
		if e <= maxstart:
			variations[e-minstart]-=1
	print(variations)
	rsum = 0
	curmax = 0
	for v in variations:
		rsum+=v
		curmax = max(curmax, rsum)
		print(rsum, curmax)
	return curmax



def get_min_max_start(times):
	curmin = float("inf")
	curmax = float("-inf")
	for start, _ in  times:
		curmin = min(curmin, start)
		curmax = max(curmax, start)
	return curmin, curmax