#O(h), O(1)


# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    lineage1_height = 0 
	lineage2_height = 0
	# calculate lineage height
	d = descendantOne
	while d:
		lineage1_height += 1
		d = d.ancestor
	
	d = descendantTwo
	while d:
		lineage2_height += 1
		d = d.ancestor
		
	younger = descendantOne if lineage1_height>=lineage2_height else descendantTwo
	older = descendantOne if lineage1_height<lineage2_height else descendantTwo
	
	for _ in range(abs(lineage1_height - lineage2_height)):
		younger = younger.ancestor
	
	while younger:
		if younger.name == older.name:
			return younger
		younger = younger.ancestor
		older = older.ancestor