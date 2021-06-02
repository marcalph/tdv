# O(n) spacetime using a stack
# reverse order of words in string w/o using split or reverse

def reverseWordsInString(string):
    # Write your code her
	
	result = []
	invert = []
	start_idx = 0
	for idx in  range(len(string)):
		if string[idx] == " ":
			invert.append(string[start_idx:idx])
			start_idx = idx+1
		else:
			continue
	invert.append(string[start_idx:])
	while invert:
		result.append(invert.pop())
    
	print(result)
	print(invert)
	return " ".join(result)