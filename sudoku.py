import sys

def copy_board(board):
    new_board = []
    for row in range(0, 9):
        new_board.append([])

        for col in range(0, 9):
            new_board[row].append(board[row][col])

    return new_board


def new_board():
    new_board = []
    for row in range(0, 9):
        new_board.append([])
        for col in range(0, 9):
            new_board[row].append(0)

    return new_board

def print_board(board):
    for row in range(0, 9):
        print ""
        for col in range(0, 9):
            value = board[row][col]
            if value == 0:
                print "_",
            else:
                print board[row][col],

    print ""

def read_file(file_path):
    board = new_board()

    board_file = open(file_path, 'r')
    row = 0
    for line in board_file:

        cols = line.split(' ')

        for col in range(0, 9):
            val = cols[col]
            if val == '_' or val == '_\n':
                board[row][col] = 0
            else:
                board[row][col] = int(cols[col])

        row = row + 1

    return board

if __name__ == "__main__":
    board = read_file(sys.argv[1])

    print "in"
    print_board(board)
