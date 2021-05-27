#O(n), O(1)

def isPalindrome(string):
    # Write your code here.
    l,r =0, len(string)-1
	while l<r:
		if string[l]!=string[r]:
			return False
		else:
			l+=1
			r-=1
	return True
