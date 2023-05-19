import abc
import typing

if typing.TYPE_CHECKING:
    from tic_tac_toe import TicTacToeException


class Player(abc.ABC):
    def __init__(self, char: str) -> None:
        self.char = char
        super().__init__()

    def __str__(self):
        return self.char

    def winning(
        self,
        coordinates: typing.Tuple[
            typing.List[None], typing.List[None], typing.List[None]
        ],
        rounds: int,
    ):
        ...

    def get_move(
        self,
        coordinates: typing.Tuple[
            typing.List[None], typing.List[None], typing.List[None]
        ],
        error: "typing.Optional[TicTacToeException]",
    ) -> typing.Tuple[int, int]:
        ...
