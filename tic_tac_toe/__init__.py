import typing

from tic_tac_toe.abc.player import Player
from tic_tac_toe.player.bot import EasyBot
from tic_tac_toe.player.human import Human


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
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        super().__init__(f"the coordinate ({x},{y}) is already taken")


class TicTacToe:

    tests: typing.List[
            typing.Tuple[
                typing.Tuple[int, int],
                typing.Tuple[int, int],
                typing.Tuple[int, int]
            ]
        ] = [
            ((0, 0), (1, 1), (2, 2)),
            ((0, 2), (1, 1), (2, 0)),
            ((0, 0), (0, 1), (0, 2)),
            ((1, 0), (1, 1), (1, 2)),
            ((2, 0), (2, 1), (2, 2)),
            ((0, 0), (1, 0), (2, 0)),
            ((0, 1), (1, 1), (2, 1)),
            ((0, 2), (1, 2), (2, 2)),
        ]

    def __init__(self, player1: Player = Human("X"), player2: Player = EasyBot("O")) -> None:
        self._coordinates: tuple[typing.List[typing.Optional[str]]] = tuple([None for _ in range(3)] for _ in range(3))
        self._players: typing.List[Player] = [player1, player2]

    @property
    def players(self):
        return self._players
    
    @property
    def coordinates(self):
        return self._coordinates

    @property
    def actual_player(self):
        return self.players[0]

    def play(self):
        winner = None

        error = None
        while winner is None:
            try:
                self.next_move(error)
                error = None
            except TicTacToeException as exc:
                error = exc.args[0]
            else:
                winner = self.test_winner(self.coordinates)

        return winner

    def _move(self, x: int, y: int, player: Player):
        if not (x in range(3)
                and y in range(3)):
            raise CoordinateExceededException()

        # x and y are inverted in the matrix
        if self._coordinates[y][x]:
            raise CoordinateOccupiedException(x, y)
        self._coordinates[y][x] = player.char

    def move(self, x, y):
        self._move(x, y, self.actual_player)

        # the player will be moved to the end of the stack
        last_player = self.players.pop(0)
        self.players.append(last_player)

    def next_move(self, error: typing.Optional[TicTacToeException]):
        player = self.players[0]
        x, y = player.get_move(self.coordinates, error)
        self.move(x, y)

    @classmethod
    def test_winner(cls, coordinates):
        
        for test in cls.tests:
            last_xy: typing.Optional[str] = None
            for i, xy in enumerate(test):
                x, y = xy
                xy = coordinates[x][y]
                if xy is None:
                    break
                if last_xy:
                    if xy != last_xy:
                        break
                    elif i == len(test) - 1:
                        return xy  
                last_xy = xy

        # if there are no empty coordinates, a tie has occurred in the TIC TAC toe
        for line in coordinates:
            for coordinate in line:
                if coordinate is None:
                    return None
                
        raise TieTicTacToe()
