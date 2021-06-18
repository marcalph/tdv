# measure something between L and H
# with a bunch of (l,h) tuples
# recursion
# O(low*high*n), O(low*high) actually low//min l and high//min h

def ambiguousMeasurements(measuringCups, low, high):
	memo = {}
	return helper(measuringCups, low, high, memo)

def helper(measuringCups, low, high, memo):
	key = createMemoKey(low, high)
	if key in memo:
		return memo[key]
    # base case    
	if high<0:
		return False

	if low<=0 and high>=0:
		return True
	# recursion
	for cup in measuringCups:
		l, h = cup
		possible = helper(measuringCups, low-l, high-h, memo)
		memo[key]=possible
		if possible:
			return True
		else:
			continue
	return False
		
	
def createMemoKey(low, high):
	return str(low)+":"+str(high)