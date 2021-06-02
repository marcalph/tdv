#O(wn log n ) , O(wn)
def groupAnagrams(words):
    # Write your code here.
	res = {}
    for word in words:
		res["".join(sorted(word))] = res.get("".join(sorted(word)), [])+[word]
	return list(res.values())
