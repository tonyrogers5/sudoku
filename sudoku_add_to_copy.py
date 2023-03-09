# Write your solution here
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    new_sudoku = []
    for row in sudoku:
        new_sudoku.append(row[:])
    new_sudoku[row_no][column_no] = number
    return new_sudoku

