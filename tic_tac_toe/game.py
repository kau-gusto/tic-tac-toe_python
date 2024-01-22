import typing
from .abc.player import Player
from .board import Board, TicTacToeException
from .player.ia import EasyBot, IntermediaryBot


class TicTacToe:
    def __init__(
        self, player1: Player = EasyBot("X"), player2: Player = IntermediaryBot("O")
    ) -> None:
        self._player1 = player1
        self._player2 = player2
        self.reset()

    @property
    def rounds(self):
        return self._rounds

    @property
    def players(self):
        return self._players

    @property
    def board(self):
        return self._board

    @property
    def actual_player(self):
        return self.players[0]

    def reset(self):
        self._board = Board()
        self._rounds = 0
        self._players: typing.List[Player] = [self._player1, self._player2]

    def play(self):
        winner = None
        error = None
        self.reset()
        while winner is None:
            try:
                self.next_move(error)
                error = None
            except TicTacToeException as exc:
                error = exc
            else:
                winner = self.board.get_winner()

        return winner

    def next_move(self, error: typing.Optional[TicTacToeException]):
        coordinate = self.actual_player.get_move(self.board, error)
        self.board.make_move(self.actual_player, coordinate)

        # the player will be moved to the end of the stack
        last_player = self.players.pop(0)
        self.players.append(last_player)
        self._rounds += 1
