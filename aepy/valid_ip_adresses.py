#O(1) spacetime
# create valid ip adresses
#generate subparts sequentially and appen d if valid
def validIPAddresses(string):
    # Write your code here.
	res = []
	for i in range(1, min(len(string),4)):
		candidate = [None, None, None, None]
		if is_valid_subpart(string[:i]):
			candidate[0] = string[:i]
			
			for j in range(i+1, i+min(len(string)-i, 4)):
				if is_valid_subpart(string[i:j]):
					candidate[1] = string[i:j]
					
					for k in range(j+1, j+min(len(string)-j,4)):
						if is_valid_subpart(string[j:k]):
							if is_valid_subpart(string[k:]):
								candidate[2] = string[j:k]
								candidate[3] = string[k:]
								res.append('.'.join(candidate))
								print(candidate)
    return res



def is_valid_subpart(string):
	asint = int(string)
	if asint > 255:
		return False
	return len(str(asint))==len(string)