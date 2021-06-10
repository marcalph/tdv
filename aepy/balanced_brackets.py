#O(n) spacetime
# check validity of various brackets
# order matters! >> think stack or queue
def balancedBrackets(string):
    # Write your code here.
	stack = []
	mapping = {
		"(":")",
		"{":"}",
		"[":"]"
	}
	for i  in range(len(string)):
		char = string[i]
		if char in "([{":
			stack.append(char)
		elif char in "}])":
			if len(stack)==0:
				# more closing than opening
				return False
			if char != mapping[stack.pop()]:
				# order is wrong
				return False		
			else:
				continue
	
	return len(stack)==0 #check for more opening than closing