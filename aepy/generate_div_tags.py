# generate valid parenthesis sequence
# brute force sequence generation and validate
#O(2^n), O((2n)!/(n!(n+1)!)) >> catalan number
#recursion
def generateDivTags(numberOfTags):
    # Write your code here
	res = []
	generate_and_store(numberOfTags, res, "")
    return adapt_sample(res)


def adapt_sample(result):
	for i in range(len(result)):
		result[i] = result[i].replace("(", "<div>").replace(")","</div>")
	return result

def is_valid(string):
	""" returns true if string is valid
		<div> is (
		</div> is )
	"""
	stack = []
	for char in string:
		if char == "(":
			stack.append("(")
		elif char ==")":
			if len(stack)==0:
				return False
			if stack[-1]!="(":
				return False
			else:
				stack.pop()
	return len(stack)==0


def generate_and_store(number, result, candidate):
	# base case
	if len(candidate)==2*number:
		if is_valid(candidate):
			result.append(candidate)
		return
	# recurrence
	generate_and_store(number, result, candidate+"(")
	generate_and_store(number, result, candidate+")")
	return None


#better recursion
#O((2n)!/(n!(n+1)!)) spacetime
def generateDivTags(numberOfTags):
    # Write your code here.
	res = []
	helper("", res, numberOfTags, numberOfTags)
    return [s.replace("(", "<div>").replace(")", "</div>") for s in res]


def helper(current, result, num_open, num_closed):
	if num_open>0:
		cur = current+'('
		helper(cur, result, num_open-1, num_closed)
	
	if num_closed>num_open:
		cur = current+')'
		helper(cur, result, num_open, num_closed-1)
	
	if num_closed==0:
		print(current)
		result.append(current)