
#O(nd), O(n)
def numberOfWaysToMakeChange(n, denoms):
    # todo 
	# order odesn't matter 1+5 approx 5+1
	ways = (n+1) * [0]
	ways[0] = 1
	
	for denom in denoms:
		for amount in range(1,n+1):
			if denom<=amount:
				ways[amount]+=ways[amount-denom]
	return ways[n]