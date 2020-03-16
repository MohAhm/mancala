from move import Move


class Player:
    def __init__(self, player):
        self.player = player

    def turn(self):
        # Return the player whose move it is in this state
        return self.player

    def other(self):
        return Player(1) if self.player == 2 else Player(2)

    def holes(self, board):
        return Move(board[:6]) if self.player == 1 else Move(board[7:13])

    def store(self):
        return 6 if self.player == 1 else 13

    def score(self, board):
        return board[self.store()]
