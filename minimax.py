from mancala import Mancala


class Minimax:
    def __init__(self, game, depth=3):
        self.game = game
        self.depth = depth

    def alpha_beta_search(self, state):
        # Returns the best action
        best_score = float('-inf')
        beta = float('inf')
        best_action = -1

        for a in self.game.actions(state):
            v = self.min_value(self.game.result(state, a), best_score, beta, 0)
            # print(best_score)
            if v > best_score:
                best_score = v
                best_action = a

        return best_action

    def max_value(self, state, alpha, beta, depth):
        # Returns a utility value
        if depth > self.depth or self.game.terminal_test(state):
            return self.game.utility(state)

        v = float('-inf')
        for a in self.game.actions(state):
            v = max(v, self.min_value(self.game.result(
                state, a), alpha, beta, depth + 1))

            if v >= beta:
                return v
            alpha = max(alpha, v)

        return v

    def min_value(self, state, alpha, beta, depth):
        # Returns a utility value
        if depth > self.depth or self.game.terminal_test(state):
            return self.game.utility(state)

        v = float('inf')
        for a in self.game.actions(state):
            v = min(v, self.max_value(self.game.result(
                state, a), alpha, beta, depth + 1))
            # print(v)
            if v <= alpha:
                return v
            beta = min(beta, v)

        return v
