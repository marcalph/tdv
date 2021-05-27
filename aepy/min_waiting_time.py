# O(n^2), O(1) space
def minimumWaitingTime(queries):
    # Write your code here.
    queries.sort()
	s = 0 
	for i in range(len(queries[:-1])):
		s+=sum(queries[:i+1])
	return s

# O(nlogn) time | O(1) space - where n is the number of queries
# decompose sum as product!
def minimumWaitingTime(queries):
	queries.sort()
	totalWaitingTime = 0
	for idx, duration in enumerate(queries):
	queriesLeft = len(queries) - (idx + 1)
	totalWaitingTime += duration * queriesLeft
	return totalWaitingTime