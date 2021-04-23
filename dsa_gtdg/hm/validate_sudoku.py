# MEDIUM
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.


# can be done in one pass
# O(1) time | O(1) space
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hml = [set() for i in range(9)]
        hmc = [set() for i in range(9)] 
        hmb = [set() for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j]!=".":
                    num = int(board[i][j])
                    if  num in hmc[j] or num in hml[i] or num in hmb[(i//3)*3+j//3]:
                        return False

                    hml[i].add(num)
                    hmc[j].add(num)
                    hmb[(i//3)*3+j//3].add(num)
        return True