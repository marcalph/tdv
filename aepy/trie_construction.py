# O(n^2) spacetime
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        # Write your code here.
		for i in range(len(string)):
			node = self.root
			for j in range(i, len(string)):
				char = string[j]
				if char not in node:
					node[char] = {}
				node = node[char]
			node[self.endSymbol]=True

		print(self.root)
		
		
    def contains(self, string):
        # Write your code here.
        node = self.root
		for char in string:
			if char not in node:
				return False
			node = node[char]
		return self.endSymbol in node