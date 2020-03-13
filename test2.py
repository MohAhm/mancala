from mancala import Mancala, Move

init_board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
board2 = [0, 5, 5, 1, 6, 5, 1, 5, 0, 5, 5, 5, 5, 0]

mancala = Mancala(board2)
state = mancala.initial
print(mancala.actions(state))
moves = mancala.actions(state)
print(mancala.to_move(state, moves[1]))

# move = Move(board2[7:13])
# print(move.possible_moves())
# print(move.to_move(2))
