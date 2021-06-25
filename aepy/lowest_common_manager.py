# get lowest common ancestor for two searched nodes nodes
# O(n), O(d)
# dfs postorder,
# initailly ancestor is None, propagate number of searched nodes found, if number met just set ancestor and propagate upwards

def getLowestCommonManager(topManager, reportOne, reportTwo):
    # Write your code here.
	return traverse(topManager, reportOne, reportTwo).lowest_mngr



def traverse(node, p, q):
	#base case
	if node is None:
		return info(node, 0)
	# recurrence
	num_reports = 0
	for child in node.directReports:
		childinfo=traverse(child, p, q)
		num_reports+=childinfo.num_reports
		if childinfo.lowest_mngr:
			print("yolo")
			print(info(childinfo.lowest_mngr, 42))
			return info(childinfo.lowest_mngr, 42)
		
	if node.name == p.name or node.name==q.name:
		num_reports+=1
	
	mngr = node if num_reports==2 else None
	return info(mngr, num_reports)



from collections import namedtuple
info = namedtuple("info", "lowest_mngr, num_reports")

# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []