# O(nlogn), O(1) space
def minimumWaitingTime(queries):
    # Write your code here.
    queries.sort()
	s = 0 
	for i in range(len(queries[:-1])):
		s+=sum(queries[:i+1])
	return s