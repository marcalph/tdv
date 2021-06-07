
# O(nm) spacetime
# dp
# 
def levenshteinDistance(str1, str2):
    # Write your code here.
	edits = [[x for x in range(len(str1)+1)] for y in range(len(str2)+1)]

	for r in range(1,len(str2)+1):
		edits[r][0] = edits[r-1][0]+1
	print(edits)
	for r in range(1, len(str2)+1):
		for c in range(1, len(str1)+1):
			if str1[c-1] == str2[r-1]:
				edits[r][c] = edits[r-1][c-1]
			else:
				edits[r][c] = 1+ min(edits[r][c-1],edits[r-1][c-1],edits[r-1][c])
	print(edits)
	return edits[-1][-1]
