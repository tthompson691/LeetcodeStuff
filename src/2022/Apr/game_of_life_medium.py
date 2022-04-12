from wrappers import time_it
import copy

def game_of_life(board):
    """
    Do not return anything, modify board in-place instead.
    """
    def check_neighbors(_i, _j):
        return sum([
            board2[a][b] for a in range(_i-1, _i+2)
            for b in range(_j-1, _j+2) 
            if not (a == _i and b == _j)
            and 0 <= a <= len(board2) - 1
            and 0 <= b <= len(board2[_i]) - 1
        ])

    board2 = [
        [y for y in i] for i in board
    ]

    for i, x in enumerate(board2):
        for j, y in enumerate(x):
            live = check_neighbors(i, j)
            if y == 1 and live < 2:
                board[i][j] = 0
                continue
            elif y == 1 and live in [2, 3]:
                board[i][j] = 1
                continue
            elif y == 1 and live > 3:
                board[i][j] = 0
                continue
            elif y == 0 and live == 3:
                board[i][j] = 1
                continue


if __name__ == "__main__":
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    game_of_life(board)
    
    