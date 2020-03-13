
class GameState:
    def __init__(self, board, player, moves, utility):
        self.board = board
        self.player = player
        self.moves = moves
        self.utility = utility

    def find_winning_move(self, game_state, next_player):
        ### A function that finds a move that immediately wins the game ###
        pass
        # 1 Loops over all legal moves
        # 2 Calculates what the board would look like if you play this move
        # 3 Does your opponent have a good defense? If not, pick this move.
        # 4 No matter what move you pick, your opponent can prevent a win.
