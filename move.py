

class Move:
    def __init__(self, pockets):
        self.moves = {}

        # Hash index 0 to move 1, index 1 to move 2 etc.
        for i, pocket in enumerate(pockets):
            if pocket is not 0:
                self.moves[i] = i + 1

    def possible_moves(self):
        return list(self.moves.keys())

    def get_move(self, key):
        return self.moves.pop(key)
