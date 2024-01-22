import abc
import typing


if typing.TYPE_CHECKING:
    from ..game import TicTacToeException
    from ..game import Board


class Player(abc.ABC):
    def __init__(self, char: str) -> None:
        self.char = char
        super().__init__()

    def __str__(self):
        return self.char

    def get_move(
        self,
        coordinates: 'Board',
        error: "typing.Optional[TicTacToeException]",
    ) -> int:
        ...

