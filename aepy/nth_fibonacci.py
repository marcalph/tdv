#O(2**n) spacetime
def getNthFib(n):
    # Write your code here.
	if n==1:
		return 0
	elif n==2:
		return 1
	else:
		return getNthFib(n-1)+getNthFib(n-2)

#O(n) spacetime) w/ memoization
def getNthFib(n, memo = {1:0, 2:1}):
	if n in memo:
		return memo[n]
	else:
		memo[n] = getNthFib(n-1, memo)+getNthFib(n-2, memo)
		return memo[n]

#O(n)time | O(1)space W/ smart iteration



