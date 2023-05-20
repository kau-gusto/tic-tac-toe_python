import abc
import typing


if typing.TYPE_CHECKING:
    from tic_tac_toe import TicTacToeException
    from tic_tac_toe import ListCoordinatesType


class Player(abc.ABC):
    def __init__(self, char: str) -> None:
        self.char = char
        super().__init__()

    def __str__(self):
        return self.char

    def winning(
        self,
        coordinates: 'ListCoordinatesType',
        rounds: int,
    ):
        ...

    def get_move(
        self,
        coordinates: 'ListCoordinatesType',
        error: "typing.Optional[TicTacToeException]",
    ) -> int:
        ...

