# import numpy as np


init_board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

board1 = [4, 4, 4, 0, 5, 5, 1, 5, 4, 4, 4, 4, 11, 0]
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

# print(board2[7:])
# print(board2[:-1])  # the last one
# print(board2[0])
# print(board2[1])
# print(len(board1))

# 0     4 4 4 4 4 4
#       4 4 0 5 5 5    1


print(board1[7:13])
print(board2[7:13])

# print(board2[7:13].index(5))
# moves = [x for x in enumerate(board2[7:13], 1) if x is not 0]

# print(board1[:7])
# print(np.flip(board1[7:13]))
# print(board1[7:13])
# print(board1[-7:-1])

# board1 = np.reshape(board1, (2, 7))
# board2 = np.reshape(board2, (2, 7))
# board[1] = np.flip(board[1])
# print(board1)
# print(board2)
# print(np.flip(board[1]))

# print(board1[9])
print(board2)

# end = 6
# print(len(board1))
# hole = 0
# skip = 0
# for i in range(pick, stones+pick):
#     # while stones > 0:
#     # hole += 1

#     if i >= len(board1):
#         i -= len(board1)

#     print(i)
# if hole == mid:
#     skip += 1
#     continue
# else:
#     hole = hole + skip

#     if hole >= len(board1):
#         hole -= len(board1)
# board1[hole] += 1

# print(board1[hole])

# print(board1)


# pocket = 12
# stones = board1[pocket]
# board1[pocket] = 0

# while stones > 0:
#     pocket = (pocket + 1) % len(board1)
#     # print(idx)
#     if pocket == 6:
#         continue

#     board1[pocket] += 1
#     stones -= 1

# print(board1)

moves = []
for i, pocket in enumerate(board2[7:13]):
    if pocket is not 0:
        moves.append(i)

print(moves)

hash = {}
for i in moves:
    hash[i] = i + 1

print(hash.values())
print(hash.get(2))
# print(hash[1])
# user_details = [{'name': x, 'rank': i}
#                 for i, x in enumerate(board2[7:13]) if x is not 0]
# print(user_details)
