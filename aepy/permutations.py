# O(n*n!) spacetime w/backtracking
# generate permutation from an array
def getPermutations(array):
    # Write your code here.    
	perms = []
	def helper(i, array, perms):
		if i == len(array)-1:
			perms.append(array[:]) # make snapshot
		else:
			for j in range(i, len(array)):
				array[i], array[j] = array[j], array[i]
				helper(i+1, array, perms)
				array[i], array[j] = array[j], array[i]
	helper(0, array, perms)
	return perms


# O(n^2*n!) , O(n*n!)
def getPermutations(array):
	perms =[]
	helper(array, perm, perms)
	return perms

def helper(array, perm, perms):
	if not len(array) and len(perm):
		perms.append(perm)
	else:
		for i in range(array):
			new_array = array[:i]+array[i+1:]
			new_perm = perm + [arrya[i]]
			helper(new_array, new_perm, perms)

