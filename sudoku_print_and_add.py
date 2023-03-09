# Write your solution here
def print_sudoku(sudoku):
    for i, row in enumerate(sudoku):
        for j, square in enumerate(row):
            if square > 0:
                print(f"{square} ", end="")
            else:
                print("_ ", end="")
            if j == 2 or j == 5:
                print(" ", end="")
        print()
        if i == 2 or i == 5:
            print()

def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number

