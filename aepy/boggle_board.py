# O(ws+nm*8^s), 0(nm+ws)
# s longest word, w nb of words
# find all

def boggleBoard(board, words):
    # Write your code here.
    trie =Trie()
	trie.add_words(words)
	print(trie.root)
	result = set()
	viewed = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
	
	for i in range(len(board)):
		for j in range(len(board[0])):
			traverse(i,j, board, viewed, trie.root, result)
	print(result)
	return list(result)

	
def traverse(i,j, board, viewed, trienode, result):
	# base case
	if viewed[i][j] == True:
		return
	
	letter = board[i][j]
	if letter not in trienode:
		return
	
	
	# recurrence
	trienode = trienode[letter]
	if "*" in trienode:
		result.add(trienode["*"])
	viewed[i][j] = True	
	for nei in get_neighbors(i, j, viewed, board):
		newx, newy = nei[0], nei[1]
		traverse(newx, newy, board, viewed, trienode, result)
	viewed[i][j] = False	
	
	
	
def get_neighbors(x,y,viewed, board):
	moves = [(-1,-1),
			 (-1, 0),
			 (-1,+1),
			 (0, -1),
			 (0, +1),
			 (+1,-1),
			 (+1, 0),
			 (+1,+1),
			]
	neighbors = []
	for mv in moves:
		newx, newy = x+mv[0], y+mv[1]
		if is_valid(newx, newy, board) and not viewed[newx][newy]:
			neighbors.append((newx, newy))
	return neighbors
	
	
def is_valid(x, y, board):
	n = len(board)
	m = len(board[0])
	return 0<=x<n and 0<=y<m


class Trie():
	def __init__(self):
		self.root = {}
	
	def add_words(self, words):
		for word in words:
			node = self.root
			for letter in word:
				node[letter] = node.get(letter, {})
				node = node[letter]
			node["*"]=word