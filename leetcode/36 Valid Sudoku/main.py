"""
Determine if a 9 x 9 Sudoku board is valid. 
Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 
without repetition.

Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

"""

"""
    SOLUTIONS OBSERVATIONS
    using hashmap to determine duplicates
    O(9²) of time and space complexity
    index to determine square -> index of full matrix / 3, because we have 9 3x3 grid
"""
import collections


def isValidSudoku(board):
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set) # key = (r/3, c/3)

    for row in range(9):
        for col in range(9):
            item = board[row][col]

            if item == ".":
                continue
            
            if (item in rows[row] or item in cols[col] or
                item in squares[(row // 3, col // 3)]):
                return False

            cols[col].add(item)
            rows[row].add(item)
            squares[(row // 3, col // 3)].add(item)

    return True


if __name__== "__main__":
    board = [[".","8","7","6","5","4","3","2","1"],
            ["2",".",".",".",".",".",".",".","."],
            ["3",".",".",".",".",".",".",".","."],
            ["4",".",".",".",".",".",".",".","."],
            ["5",".",".",".",".",".",".",".","."],
            ["6",".",".",".",".",".",".",".","."],
            ["7",".",".",".",".",".",".",".","."],
            ["8",".",".",".",".",".",".",".","."],
            ["9",".",".",".",".",".",".",".","."]]

    print(isValidSudoku(board))

