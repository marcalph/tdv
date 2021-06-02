
#O(n*l) , O(c) c distinct chars
# keep track of running max freq observed
def minimumCharactersForWords(words):
    # Write your code here.
	from collections import Counter
	if len(words)<=0:
		return []
	cnt = Counter(words[0])
	for i in range(1,len(words)):
		state = cnt.copy()
		for letter in words[i]:
			state[letter] = state.get(letter, 0) - 1
		for letter in state:
			if state[letter]<0:
				cnt[letter]  = cnt.get(letter, 0) - (state[letter])
	res=[]
	for k, mul in cnt.items():
		res.extend([k]*mul)
	return res