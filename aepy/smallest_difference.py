
#O(nlogn+mlogm) time | O(1) space
def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
	arrayOne.sort()
	arrayTwo.sort()
	p1, p2 = 0, 0
	curmin = float("inf")
	diff = float("inf")
	res_pair=[arrayOne[p1], arrayTwo[p2]]
	while p1<len(arrayOne) and p2<len(arrayTwo):
		num1 = arrayOne[p1]
		num2 = arrayTwo[p2]
		if num1<num2:
			p1 += 1
		elif num1>num2:
			p2 += 1
		else:
			return [num1, num2]
		
		diff=abs_diff(num1, num2)
		if curmin>diff:
			curmin = diff
			res_pair = [num1, num2]
			print(res_pair)
	return res_pair

def abs_diff(a,b):
	return max(a,b)-min(a,b)