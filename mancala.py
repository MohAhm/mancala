from player import Player


class GameState:
    def __init__(self, player, moves, board, utility):
        self.player = player
        self.moves = moves
        self.board = board
        self.utility = utility


class Mancala:
    def __init__(self, board, player_turn):
        player = Player(player_turn)
        moves = player.holes(board)

        self.initial = GameState(player, moves, board, 0)

    def actions(self, state):
        # Return a list of legal moves for a state
        return state.moves.possible_moves()

    def result(self, state, move):
        # Return the state that results from making a move from a state
        board = state.board.copy()

        board, curr_hole = self.move_stone(board, move, state.player)
        oppo_hole = 12 - curr_hole
        start_idx, end_idx = state.player.side()
        if board[curr_hole] == 1 and curr_hole in range(start_idx, end_idx) and board[oppo_hole] > 0:
            board = self.capture(board, state.player, curr_hole, oppo_hole)

        if not state.player.holes(board).possible_moves():
            board = self.capture_all(board, state.player)

        # If the last stone is dropped in the player store, get a free turn.
        if (state.player.turn() == 1 and curr_hole == 6) or (state.player.turn() == 2 and curr_hole == 13):
            player_turn = state.player
        else:
            player_turn = state.player.other()

        moves = player_turn.holes(board)

        return GameState(player_turn, moves, board, 0)

    def move_stone(self, board, move, player):
        # Deposits one of the stones in each hole until the stones run out
        if player.turn() == 2:
            move = move + 7

        stones = board[move]
        board[move] = 0
        curr_hole = move

        while stones > 0:
            curr_hole = (curr_hole + 1) % len(board)

            if player.turn() == 2 and curr_hole == 6:
                continue
            if player.turn() == 1 and curr_hole == 13:
                continue

            board[curr_hole] += 1
            stones -= 1

        return board, curr_hole

    def capture(self, board, player, curr_hole, oppo_hole):
        # If the last stone is dropped in an empty hole capture the stones in the opposite hole
        if curr_hole is player.store():
            return board

        stone = board[curr_hole]
        stones = board[oppo_hole]
        board[curr_hole] = 0
        board[oppo_hole] = 0

        board[player.store()] += stones + stone

        return board

    def capture_all(self, board, player):
        # If the player side get empty, the other player capture all stones that is left
        player_turn = player.other()
        start_idx, end_idx = player_turn.side()
        store = player_turn.store()

        board[store] += sum(board[start_idx:end_idx])
        for i in range(start_idx, end_idx):
            board[i] = 0

        return board

    def apply_move(self, state, key):
        return str(state.moves.get_move(key))

    # def terminal_test(self, state):
    #     """A state is terminal if it is won or there are no empty squares."""
    #     return state.utility != 0 or len(state.moves) == 0

    # def utility(self, state, player):
    #     """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""
    #     return state.utility if player == 'X' else -state.utility
