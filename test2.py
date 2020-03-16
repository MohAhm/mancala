from mancala import Mancala, Player

playerTurn = 2

init_board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
board2 = [0, 5, 5, 1, 6, 5, 1, 5, 0, 5, 5, 5, 5, 0]
# 0     5 5 5 5 0 5
#       0 5 5 1 6 5    1

board3 = [0, 5, 5, 1, 6, 5, 8, 0, 0, 0, 0, 0, 1, 18]
# 18     1 0 0 0 0 0
#       0 5 5 1 6 5    8

mancala = Mancala(init_board, playerTurn)
state = mancala.initial

# print(mancala.actions(state))
print(state.board)
moves = mancala.actions(state)

for move in moves:
    s = mancala.result(state, move)
    # print(s.player.turn())
    print(s.board)

# print(mancala.apply_move(state, moves[1]))
# print(state.player.turn())
# print(moves)
# state = mancala.result(state, moves[4])
# print(mancala.actions(state))
# print(state.board)
# print(state.player.turn())
# print(state.player.score(state.board))
