# interweavings of two string (with order of each of them maintenained) equals third string?
# recursion
# O(2^(n+m)), O(n+m)
# O(nm) spacetime with caching
def interweavingStrings(one, two, three):
    # Write your code here.
	if len(one)+len(two)!=len(three): 
		return False
	return traverse(one, two, three, 0, 0)

def traverse(one, two, three, i, j):
	print(one[i:], two[j:], three[min(len(three)-1, i+j)])
	k = i+j
	if k==len(three):
		return True
	
	if i<len(one) and one[i]==three[k]:	
		if traverse(one, two, three, i+1, j):
			return True
	if j<len(two) and two[j]==three[k]:
		if traverse(one, two, three, i, j+1):
			return True
	return False
	
	
# caching
def interweavingStrings(one, two, three):
    # Write your code here.
	if len(one)+len(two)!=len(three): 
		return False
	cache = [[None for _ in range(len(one)+1)] for _ in range(len(two)+1)]
	from pprint import pprint 
	return traverse(one, two, three, 0, 0, cache)


def traverse(one, two, three, i, j, cache):
	if cache[j][i] is not None:
		return cache[j][i]
	else:
		k = i+j
		if k==len(three):
			return True

		if i<len(one) and one[i]==three[k]:	
			if traverse(one, two, three, i+1, j, cache):
				cache[j][i] = True
				return cache[j][i] 

		if j<len(two) and two[j]==three[k]:
			if traverse(one, two, three, i, j+1, cache):
				cache[j][i] = True
				return cache[j][i] 
		
		cache[j][i]=False
		return cache[j][i] 
	