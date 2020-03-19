from mancala import Mancala

playerTurn = 2
board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
# board = [0, 5, 5, 1, 6, 5, 8, 0, 0, 0, 1, 0, 1, 18]
# board = [0, 0, 0, 0, 6, 0, 8, 1, 0, 5, 5, 5, 0, 18]
# board = [0, 0, 6, 5, 10, 0, 8, 1, 0, 5, 5, 5, 0, 18]
# board = [0, 5, 5, 1, 6, 5, 1, 5, 0, 5, 5, 5, 5, 0]
# board = [0, 5, 5, 1, 6, 5, 1, 5, 0, 5, 5, 5, 5, 0]

mancala = Mancala(board, playerTurn)
state = mancala.initial

print(state.board)


# for move in mancala.actions(state):
#     s = mancala.result(state, move)
#     print(s.board)


def minmax_decision(state, game, depth=4):
    """Given a state in a game, calculate the best move by searching
    forward all the way to the terminal states. [Figure 5.3]"""

    def max_value(state, depth):
        if depth == 0 or game.terminal_test(state):
            return game.utility(state)
        value = float('-inf')
        for a in game.actions(state):
            result = min_value(game.result(state, a), depth - 1)
            value = max(value, result)
        return value

    def min_value(state, depth):
        if depth == 0 or game.terminal_test(state):
            return game.utility(state)
        value = float('inf')
        print(state.board)
        for a in game.actions(state):
            result = max_value(game.result(state, a), depth - 1)
            # print(result)
            value = min(value, result)
            # print(value)
        return value

    # Body of minmax_decision:
    return max(game.actions(state), key=lambda a: min_value(game.result(state, a), depth))


def alpha_beta_search(state, game, depth=4):
    """Search game to determine best action; use alpha-beta pruning.
    As in [Figure 5.7], this version searches all the way to the leaves."""

    # Functions used by alpha_beta
    def max_value(state, alpha, beta, depth):
        if depth == 0 or game.terminal_test(state):
            return game.utility(state)
        v = float('-inf')
        for a in game.actions(state):
            v = max(v, min_value(game.result(state, a), alpha, beta, depth - 1))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(state, alpha, beta, depth):
        if depth == 0 or game.terminal_test(state):
            return game.utility(state)
        # print(state.board)
        v = float('inf')
        for a in game.actions(state):
            v = min(v, max_value(game.result(state, a), alpha, beta, depth - 1))
            # print(a)
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    # Body of alpha_beta_search:
    best_score = float('-inf')
    beta = float('inf')
    best_action = None
    for a in game.actions(state):
        v = min_value(game.result(state, a), best_score, beta, depth)
        if v > best_score:
            best_score = v
            best_action = a
    return best_action


def alpha_beta_cutoff_search(state, game, d=4, cutoff_test=None, eval_fn=None):
    """Search game to determine best action; use alpha-beta pruning.
    This version cuts off search and uses an evaluation function."""

    # Functions used by alpha_beta
    def max_value(state, alpha, beta, depth):
        if cutoff_test(state, depth):
            return eval_fn(state)
        v = float('-inf')
        for a in game.actions(state):
            if state.player.turn() == 1:
                v = max(v, max_value(game.result(
                    state, a), alpha, beta, depth + 1))
            else:
                v = max(v, min_value(game.result(
                    state, a), alpha, beta, depth + 1))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(state, alpha, beta, depth):
        if cutoff_test(state, depth):
            return eval_fn(state)
        v = float('inf')
        for a in game.actions(state):
            if state.player.turn() == 1:
                v = min(v, max_value(game.result(
                    state, a), alpha, beta, depth + 1))
            else:
                v = min(v, min_value(game.result(
                    state, a), alpha, beta, depth + 1))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    # Body of alpha_beta_cutoff_search starts here:
    # The default test cuts off at depth d or at a terminal state
    cutoff_test = (cutoff_test or (lambda state, depth: depth >
                                   d or game.terminal_test(state)))
    eval_fn = eval_fn or (lambda state: game.utility(state))
    best_score = float('-inf')
    beta = float('inf')
    best_action = None
    for a in game.actions(state):
        v = min_value(game.result(state, a), best_score, beta, 1)
        if v > best_score:
            best_score = v
            best_action = a
    return best_action


# test = minmax_decision(state, mancala)
# test = alpha_beta_search(state, mancala)
test = alpha_beta_cutoff_search(state, mancala)
print(test)
