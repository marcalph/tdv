#O(nd), O(n) 
def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    ways = (n+1) * [float("inf")]
	ways[0]=0
	for i in range(len(ways)):
		for denom in denoms:
			if denom<=i:
				ways[i] = min(ways[i], ways[i-denom]+1)
	print(ways)
	return ways[n] if ways[n]!= float("inf") else -1
	