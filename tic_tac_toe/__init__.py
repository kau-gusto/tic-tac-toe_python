import typing

from tic_tac_toe.abc.player import Player
from tic_tac_toe.player.bot import EasyBot
from tic_tac_toe.player.human import Human
from tic_tac_toe.datasets import tests


class TicTacToeException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class TieTicTacToe(TicTacToeException):
    def __init__(self) -> None:
        super().__init__("there was a tie on the TIC TAC toe")


class CoordinateExceededException(TicTacToeException):
    def __init__(self) -> None:
        super().__init__("x and y must be between 0 and 2")


class CoordinateOccupiedException(TicTacToeException):
    def __init__(self, coordinate: int) -> None:
        self.coordinate = coordinate
        super().__init__(f"the coordinate ({coordinate}) is already taken")


CoordinateType = typing.Union[int, Player]
ListCoordinatesType = typing.List[CoordinateType]


class TicTacToe:
    def __init__(
        self, player1: Player = Human("X"), player2: Player = EasyBot("O")
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
    def coordinates(self):
        return self._coordinates

    @property
    def actual_player(self):
        return self.players[0]

    def reset(self):
        self._coordinates: ListCoordinatesType = list(range(9))
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
                winner = self.test_winner(self.coordinates)

        winner.winning(self.coordinates, self.rounds)
        return winner

    def _move(self, player: Player, coordinate: int):
        if not (coordinate in range(9)):
            raise CoordinateExceededException()

        # x and y are inverted in the matrix
        if isinstance(self._coordinates[coordinate], Player):
            raise CoordinateOccupiedException(coordinate)
        self._coordinates[coordinate] = player

    def move(self, player: Player, coordinate: int):
        self._move(player, coordinate)

        # the player will be moved to the end of the stack
        last_player = self.players.pop(0)
        self.players.append(last_player)
        self._rounds += 1

    def next_move(self, error: typing.Optional[TicTacToeException]):
        coordinate = self.actual_player.get_move(self.coordinates, error)
        self.move(self.actual_player, coordinate)

    @classmethod
    def test_winner(cls, coordinates: ListCoordinatesType):
        has_empty = False
        for test in tests:
            a_coordinate, b_coordinate, c_coordinate = test
            a, b, c = (
                coordinates[a_coordinate],
                coordinates[b_coordinate],
                coordinates[c_coordinate],
            )
            if isinstance(b, Player) and a == b and b == c:
                return b

            # if there are no empty coordinates, a tie has occurred in the TIC TAC toe
            if isinstance(a, int) or isinstance(b, int) or isinstance(c, int):
                has_empty = True

        if not has_empty:
            raise TieTicTacToe()
        return None
