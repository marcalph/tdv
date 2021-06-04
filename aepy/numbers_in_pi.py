# O(n^3+m), O(n+m), n pi m numbers size
# dp + recursion + caching
# split string in eligibles subparts using minimum number of splits
def numbersInPi(pi, numbers):
    # Write your code here.
    numbers = {n: True for n in numbers}
	cache = {}
	min_spaces = get_min_spaces(pi, numbers, cache, 0)
	return -1 if min_spaces == float("inf") else min_spaces
	
def get_min_spaces(pi, numbers, cache, idx):
	if idx == len(pi):
		return -1 # to cancel out the end space
	
	if idx in cache:
		return cache[idx]
	
	min_spaces = float("inf")
	for i in range(idx, len(pi)):
		prefix = pi[idx:i+1]
		if prefix in numbers:
			min_spaces_in_suffix = get_min_spaces(pi, numbers, cache, i+1)
			min_spaces = min(min_spaces, min_spaces_in_suffix+1)
	cache[idx] = min_spaces
	return cache[idx]