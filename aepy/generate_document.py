#O(m+n) time | O(c) space where m len(characters)
#                               n len(document)
#                               c len(set(characers))

def generateDocument(characters, document):
    # Write your code here.
    viewed = {}
	for c in characters:
		viewed[c]=viewed.get(c,0)+1
	for c in document:
		if c in viewed:
			viewed[c]-=1
		else:
			return False
	return viewed[min(viewed, key=viewed.get)]>=0
