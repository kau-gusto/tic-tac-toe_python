from random import random
import typing

from tic_tac_toe.abc.player import Player

if typing.TYPE_CHECKING:
    from tic_tac_toe import TicTacToeException


class EasyBot(Player):

    def get_move(self,
                 coordinates: typing.Tuple[typing.List[None], typing.List[None], typing.List[None]],
                 error: 'typing.Optional[TicTacToeException]') -> typing.Tuple[int, int]:
        x = round(random() * 2)
        y = round(random() * 2)

        return (x, y)
    