
# O(n) spacetime
def runLengthEncoding(string):
    # Write your code here.
	viewed ={}
	prev= None
	res = []
	count=0
	for c in string:
		if count==9:
			res.append(f"{count}{prev}")
			count=0
		if prev==c:
			count+=1
		else:
			if prev is not None and count>0:
				res.append(f"{count}{prev}")
			count=1
			prev=c
	res.append(f"{count}{c}")
	return "".join(res)