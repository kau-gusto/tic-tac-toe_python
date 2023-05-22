import abc
import typing


if typing.TYPE_CHECKING:
    from tic_tac_toe import TicTacToeException
    from tic_tac_toe import Board


class Player(abc.ABC):
    def __init__(self, char: str) -> None:
        self.char = char
        super().__init__()

    def __str__(self):
        return self.char

    def winning(
        self,
        coordinates: 'Board',
        rounds: int,
    ):
        ...

    def get_move(
        self,
        coordinates: 'Board',
        error: "typing.Optional[TicTacToeException]",
    ) -> int:
        ...

