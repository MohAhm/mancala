# import numpy as np
from mancala import Mancala, Player

init_board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

board1 = [4, 4, 4, 0, 5, 5, 1, 5, 4, 4, 4, 4, 4, 0]
# 0     4 4 4 4 4 5
#       4 4 4 0 5 5    1

board2 = [0, 5, 5, 1, 6, 5, 1, 5, 0, 5, 5, 5, 5, 0]
# 0     5 5 5 5 0 5
#       0 5 5 1 6 5    1

# Player 1: moved 6
# 0     4 4 4 5 5 5
#       4 4 4 4 4 0    1
# Player 2: moved 6
# 1     0 4 4 4 4 4
#       5 5 5 4 4 4    0
# Player 2: moved 1
# 0     4 5 5 5 5 0
#       4 4 4 4 4 4    0

print(board2)
# print(board2[:6])
# print(board2[7:13])
# print(board2[6])
print(board2[4])
print(board2[8])

# move = 5
# move = move + 7
# print(move)


# 5 = 12
# 4 = 11
# 3 = 10
# 2 = 9
# 1 = 8
# 0 = 7

# 5 = 7
# 4 = 8
# 3 = 9
# 2 = 10
# 1 = 11
# 0 = 12
