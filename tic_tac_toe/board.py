import typing

from tic_tac_toe.datasets import tests
from tic_tac_toe.abc.player import Player


class TicTacToeException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class TieTicTacToe(TicTacToeException):
    def __init__(self) -> None:
        super().__init__("there was a tie on the TIC TAC toe")


class CoordinateExceededException(TicTacToeException):
    def __init__(self) -> None:
        super().__init__("the coordinate must be between 0 and 8")


class JustPlayedException(TicTacToeException):
    def __init__(self, player: Player) -> None:
        self.player = player
        super().__init__(f"player '{player}' cannot play again")


class CoordinateOccupiedException(TicTacToeException):
    def __init__(self, coordinate: int) -> None:
        self.coordinate = coordinate
        super().__init__(f"the coordinate ({coordinate}) is already taken")


ItemType = typing.Union[int, "Player"]
ListBoardType = typing.List[ItemType]

_T = typing.TypeVar("_T")


class Board:
    def __init__(self) -> None:
        self._board: ListBoardType = list(range(9))
        self._last_player: typing.Optional[Player] = None

    def __len__(self):
        return self._board.__len__()

    def __iter__(self):
        return self._board.__iter__()

    def __getitem__(self, __i: int):
        return self._board.__getitem__(__i)

    def __setitem__(self, __key: int, __value: Player):
        self.make_move(__value, __key)

    @property
    def board(self):
        return self._board

    def make_move(self, player: Player, coordinate: int):
        if not (coordinate in range(9)):
            raise CoordinateExceededException()

        # x and y are inverted in the matrix
        if isinstance(self._board[coordinate], Player):
            raise CoordinateOccupiedException(coordinate)

        if self._last_player and self._last_player == player:
            raise JustPlayedException(player)
        self._board[coordinate] = player
        self._last_player = player

    @classmethod
    def test_winner(cls, board: ListBoardType):
        has_empty = False
        for test in tests:
            a_coordinate, b_coordinate, c_coordinate = test
            a, b, c = (
                board[a_coordinate],
                board[b_coordinate],
                board[c_coordinate],
            )
            if isinstance(b, Player) and a == b and b == c:
                return b

            # if there are no empty coordinates, a tie has occurred in the TIC TAC toe
            if isinstance(a, int) or isinstance(b, int) or isinstance(c, int):
                has_empty = True

        if not has_empty:
            raise TieTicTacToe()
        return None
    
    def get_winner(self):
        return Board.test_winner(self.board)
