input = '295743861 431865927 876192543 387459216 612387495 549216738 763524189 928671354 154938672'
Sudoku = True

# create board, read lines, columns and sub boxes
board = [[i for i in x] for x in input.split()]
if sum([len(x) for x in board]) != 81:
    all = []
    Sudoku = False
else:
    line = [[board[y][x] for x in range(9)] for y in range(9)]
    column = [[board[y][x] for y in range(9)] for x in range(9)]
    sub_box = [[board[y0 * 3 + y][x0 * 3 + x] for x in range(3) for y in range(3)] for x0 in range(3) for y0 in range(3)]
    all = line + column + sub_box

# Check the sudoku
for el in all:
    tmp = [int(i) for i in el if i.isdigit() and 0 < int(i) <=9]
    Sudoku = False if not tmp else True
    if len(tmp) != 9 or sum(tmp) != 45:
        Sudoku = False
        break

print('Good! the Sudoku is Correct' if Sudoku else 'The Sudoku is Incorrect!')
