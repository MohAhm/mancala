from mancala import Mancala
from minimax import Minimax

playerTurn = 2
board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
# board = [0, 0, 0, 0, 6, 0, 8, 1, 0, 5, 5, 5, 0, 18]
# board = [0, 5, 5, 1, 6, 5, 8, 0, 0, 0, 1, 0, 1, 18]

mancala = Mancala(board, playerTurn)
state = mancala.initial
print(state.board)

minimax = Minimax(mancala)
action = minimax.alpha_beta_search(state)
print(action)
