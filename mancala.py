from game_state import GameState
from move import Move 


class Mancala:
    def __init__(self, board):
        moves = Move(board[7:13])
        self.initial = GameState(board, 1, moves, 0)

    def actions(self, state):
        # Return a list of the allowable moves
        return state.moves.possible_moves()

    def result(self, state, move):
        # Return the state that results from making a move
        stones = state.board[move]
        state.board[move] = 0

        while stones > 0:
            move = (move + 1) % len(state.board)

            if move == 6:
                continue

            state.board[move] += 1
            stones -= 1

        return state

    def to_move(self, state, key):
        return str(state.moves.get_move(key))

    # def terminal_test(self, state):
    #     """A state is terminal if it is won or there are no empty squares."""
    #     return state.utility != 0 or len(state.moves) == 0

    # def utility(self, state, player):
    #     """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""
    #     return state.utility if player == 'X' else -state.utility

    # def to_move(self, state):
    #     """Return the player whose move it is in this state."""
    #     return state.to_move

    # def apply_move(self, moves):
