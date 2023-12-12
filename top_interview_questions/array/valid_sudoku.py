"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need
to be validated
 according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits
 1-9 without repetition.
Note:
A Sudoku board (partially filled) could be valid but is not necessarily
solvable.
Only the filled cells need to be validated according to the mentioned
rules.
"""
from icecream import ic


def check_if_valid(board):
    for line in board:
        row = []
        for char in line:
            if char != '.':
                row.append(int(char))
        if len(row) != len(set(row)):
            return False
    return True


def is_box_valid(board, row, col):
    box = set()
    for i in range(3):
        for j in range(3):
            num = board[row + i][col + j]
            if num in box:
                return False
            if num != '.':
                box.add(num)
    return True


def is_valid_sudoku(board: list[list[str]]) -> bool:
    vert = {}
    for line in board:
        for i, v in enumerate(line):
            vert[i] = vert.get(i, []) + [v]

    rotated_board = []

    for v in vert.values():
        rotated_board.append(v)

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not is_box_valid(board, i, j):
                return False

    if check_if_valid(board) and check_if_valid(rotated_board):
        return True

    return False


board1 = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
          [".", "9", "8", ".", ".", ".", ".", "6", "."],
          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", "6", ".", ".", ".", ".", "2", "8", "."],
          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

board2 = [["8", "3", ".", ".", "7", ".", ".", ".", "."],
          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
          [".", "9", "8", ".", ".", ".", ".", "6", "."],
          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", "6", ".", ".", ".", ".", "2", "8", "."],
          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

board3 = [[".", ".", ".", ".", "5", ".", ".", "1", "."],
          [".", "4", ".", "3", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", "3", ".", ".", "1"],
          ["8", ".", ".", ".", ".", ".", ".", "2", "."],
          [".", ".", "2", ".", "7", ".", ".", ".", "."],
          [".", "1", "5", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", "2", ".", ".", "."],
          [".", "2", ".", "9", ".", ".", ".", ".", "."],
          [".", ".", "4", ".", ".", ".", ".", ".", "."]]

assert is_valid_sudoku(board1) is True
assert is_valid_sudoku(board2) is False
assert is_valid_sudoku(board3) is False
