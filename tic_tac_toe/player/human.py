import math
import typing

from ..abc import Player

if typing.TYPE_CHECKING:
    from ..game import TicTacToeException
    from ..board import Board

class Human(Player):

    def __init__(self, char: str, get_move: 'typing.Callable[[Human,Board, typing.Optional[TicTacToeException]], int]') -> None:
        self._get_move = get_move
        super().__init__(char)

    def get_move(
        self,
        coordinates: 'Board',
        error: "typing.Optional[TicTacToeException]",
    ) -> int:
        return self._get_move(self,coordinates, error)
