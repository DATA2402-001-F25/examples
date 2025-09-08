
my_variable = 5
my_string = "text"

my_list = ['a', 'b', 'c']
my_list[0]
my_list[-1]
my_list[1] = 'd'

two_d_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
top_left = two_d_list[0][0]
middle = two_d_list[1][1]
bottom_left = two_d_list[2][0]

tic_tac_toe_board = [
    [1, 0, 0],
    [0, 1, 0],
    [-1,-1,1],
]

def check(board: list) -> int:
    """
    documentation here
    """

    # sum up each row, checking for sums of +3 or -3
    for row_idx in range(3):
        row1_sum = sum(board[row_idx])
        if row1_sum == 3:
            return 1
        elif row1_sum == -1:
            return -1
        
    # check all the columns
    # we'll use a nested for loop for this
    for col_idx in range(3):
        this_column = []
        for row_idx in range(3):
            this_column.append(board[row_idx][col_idx])
        column_sum = sum(this_column)
            if column_sum == 3:
                return 1
            elif column_sum == -1:
                return -1

    # check diagonals
    diag1_sum = board[0][0] + board[1][1] + board[2][2]
    diag2_sum = board[2][0] + board[1][1] + board[0][2]
    
    if diag1_sum == 3:
        return 1
    elif diag1_sum == -1:
        return -1

    if diag2_sum == 3:
        return 1
    elif diag2_sum == -1:
        return -1
    
    return 0