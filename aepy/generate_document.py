#O(m+n) time | O(c) space where m len(characters)
#                               n len(document)
#                               c len(set(characers))

def generateDocument(characters, document):
    # Write your code here.
    viewed = {}
	for c in characters:
		viewed[c]=viewed.get(c,0)+1
	for c in document:
		
		if c not in viewed or viewed[c]==0:
			return False
		viewed[c]-=1
		
	return True