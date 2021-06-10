# O(n^3), O(n), can make in O(1) space by using only indices
# find palindrome in substrings
#brute force
def longestPalindromicSubstring(string):
    # Write your code here.
	current_best = ""
	for i in range(len(string)):
		for j in range(i, len(string)):
			candidate = string[i:j+1]
			if is_palindrome(candidate) and len(candidate)>len(current_best):
				current_best=candidate
	return current_best
			
			
def is_palindrome(string):
	l, r = 0, len(string)-1
	while l<r:
		if string[l]!=string[r]:
			return False
		else:
			l+=1
			r-=1
	return True


# O(n^2), 0(1)
# check starting from current char
def longestPalindromicSubstring(string):
	current_best = [0, 1]
	for i in range(1, len(string)):
		window = 1
		while 0<=i-window and i+window<len(string) and string[i-window]==string[i+window]: # validate index and palindromicity
			current_best = update_current_best(i-window, i+window, current_best)
			window+=1
			
		window = 0
		while 0<=i-1-window and i+window<len(string) and string[i-1-window]==string[i+window]:
			current_best = update_current_best(i-1-window, i+window, current_best)
			window+=1
	return string[current_best[0]:current_best[1]]
		
			
def update_current_best(l, r, current_best):
	current_best_len = current_best[1]-current_best[0]
	current_len = r - l + 1
	if current_len > current_best_len:
		current_best = [l, r+1]
	return current_best
	
		
