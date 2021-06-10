# O(n*n!) spacetime
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

# O(n^2*n!), O(n*n!)
def getPermutations(array):
	perms = []
	if len(array)==0:
		return []
	def helper(arr, perm, perms):
		if len(perm)==len(array):
			perms.append(perm)
		else:
			for i in range(len(arr)):
				new_arr = arr[:i]+arr[i+1:]
				new_perm = perm+[arr[i]]
				helper(new_arr, new_perm, perms)
	helper(array, [], perms)
	return perms