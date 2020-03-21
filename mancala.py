from player import Player


class GameState:
    def __init__(self, player, moves, board, utility):
        self.player = player
        self.moves = moves
        self.board = board
        self.utility = utility


class Mancala:
    def __init__(self, board, player_turn):
        self.player_turn = player_turn

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
        if (curr_hole in range(start_idx, end_idx) and  # check if the current hole (last stone) is in the player side
                board[curr_hole] == 1 and               # is it the last stone
                board[oppo_hole] > 0):                  # and the opposite hole is not empty
            board = self.capture(board, state.player, curr_hole, oppo_hole)

        if self.game_end(board):
            board = self.capture_all(board, state.player)

        # If the last stone is dropped in the player store, get a free turn.
        if ((state.player.turn() == 1 and curr_hole == 6) or
                (state.player.turn() == 2 and curr_hole == 13)):
            player_turn = state.player
        else:
            player_turn = state.player.other()

        moves = player_turn.holes(board)
        utility = self.eval(board, player_turn, moves)

        return GameState(player_turn, moves, board, utility)

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
        # If the player side get empty, the other player capture all remains stones
        start_idx, end_idx = player.side()
        store = player.store()
        board[store] += sum(board[start_idx:end_idx])
        for i in range(start_idx, end_idx):
            board[i] = 0

        opponent = player.other()
        start_idx, end_idx = opponent.side()
        store = opponent.store()
        board[store] += sum(board[start_idx:end_idx])
        for i in range(start_idx, end_idx):
            board[i] = 0

        return board

    def apply_move(self, state, key):
        # Convert moves from position 0 to 5 to '1' to '6'
        return str(state.moves.get_move(key))

    def terminal_test(self, state):
        # A state is terminal if one side of Mancala is empty
        return self.game_end(state.board)

    def utility(self, state):
        # Return the value to player
        return state.utility

    def eval(self, board, player, player_moves):
        # The evaluation function
        opponent = player.other()
        opponent_moves = opponent.holes(board)

        if player.turn() == self.player_turn:
            score_diff = player.score(board) - opponent.score(board)
            moves_diff = len(player_moves.possible_moves()) - \
                len(opponent_moves.possible_moves())

            return score_diff + moves_diff
        else:
            score_diff = opponent.score(board) - player.score(board)
            moves_diff = len(opponent_moves.possible_moves()) - \
                len(player_moves.possible_moves())

            return score_diff + moves_diff

    def game_end(self, board):
        # Return true if either player or opponent side is empty
        return all(hole == 0 for hole in board[:6]) or all(hole == 0 for hole in board[7:13])
