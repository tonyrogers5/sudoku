def row_correct(sudoku: list, row_no: int):
    new_list = []
    for square in sudoku[row_no]:
        if square > 0:
            new_list.append(sudoku[row_no].count(square))
    for i in new_list:
        if i > 1:
            return False
            break
    return True

def column_correct(sudoku: list, column_no: int):
    new_list = []
    new_list2 = []
    for row in sudoku:
        if row[column_no] > 0:
            new_list.append(row[column_no])
    for i in new_list:
        new_list2.append(new_list.count(i))
    for i in new_list2:
        if i > 1:
            return False
            break
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    new_list = []
    new_list2 = []
    row_range = [row_no, row_no + 1, row_no + 2]
    column_range = [column_no, column_no + 1, column_no + 2]
    for i in row_range:
        for j in column_range:
            if sudoku[i][j] > 0:
                new_list.append(sudoku[i][j])

    for i in new_list:
        new_list2.append(new_list.count(i))

    for i in new_list2:
        if i > 1:
            return False
            break
    return True

def check_grid(sudoku: list): 
    grid_index = [0, 3, 6]
    for i in grid_index:
        for j in grid_index:
            if block_correct(sudoku, i, j) == False:
                return False
                break
    return True

def row_column(sudoku: list):
    for i in range(len(sudoku[0])):
        if row_correct(sudoku, i) == False or column_correct(sudoku, i) == False:
            return False
    return True
            



def sudoku_grid_correct(sudoku: list):
    if row_column(sudoku) and check_grid(sudoku) == True:
        return True
    else:
        return False
