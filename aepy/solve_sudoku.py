#O(1) spacetime
def solveSudoku(board):
    # Write your code here.
	# generate helper structures
	partial(0,0, board)
    return board


def is_valid(num, i, j, board):
	if num in board[i] or num in map(lambda r: r[j], board):
		return False
	
	start_row = i//3*3
	start_col = j//3*3
	for ridx in range(3):
		for cidx in range(3):
			if num==board[start_row+ridx][start_col+cidx]:
				return False
	return True

def partial(i, j, board):
	if j==len(board[i]):
		i+=1
		j=0
		if i==len(board):
			return True
	
	if board[i][j]==0:
		return try_insert(i,j,board)
	return partial(i, j+1, board)

def try_insert(i,j, board):
	for num in range(1,10):
		if is_valid(num, i,j,board):
			board[i][j]=num
			if partial(i, j+1, board):
				return True
	
	board[i][j]=0
	return False