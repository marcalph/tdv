#O(n) spacetime
def getNthFib(n):
    # Write your code here.
	if n==1:
		return 0
	elif n==2:
		return 1
	else:
		return getNthFib(n-1)+getNthFib(n-2)

#O(n) spacetime) w/ memoization


#O(n)time | O(1)space W/ smart iteration



