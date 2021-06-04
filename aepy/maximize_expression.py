# O(n) spacetime
# brute force O(n^4), O(1)
# maximise arithmetic expression
# dp
# maximise one element at the time
def maximizeExpression(array):
	if len(array)<4:
		return 0
    # Write your code here.
	n = len(array)
	startmax = float("-inf")
	maxa = [array[0]]
	for i in range(1,n):
		curmax = max(maxa[i-1], array[i])
		maxa.append(curmax)
		
	maxab = [startmax]*1
	for i in range(1, n):
		curmax = max(maxab[i-1], maxa[i-1]-array[i])
		maxab.append(curmax)
		
	maxabc = [startmax]*2
	for i in range(2, n):
		curmax = max(maxabc[i-1], maxab[i-1]+array[i])
		maxabc.append(curmax)
		
	maxabcd = [startmax]*3
	for i in range(3, n):
		curmax = max(maxabcd[i-1], maxabc[i-1]-array[i])
		maxabcd.append(curmax)
	
	
	print(array)
	print(maxa)
	print(maxab)
	print(maxabc)
	print(maxabcd)
	return maxabcd[-1]