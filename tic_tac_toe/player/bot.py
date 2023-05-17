from random import random
import typing

from tic_tac_toe.abc.player import Player
from tic_tac_toe.player.human import print_coordinates
from tic_tac_toe.utils import clear

if typing.TYPE_CHECKING:
    from tic_tac_toe import TicTacToeException


class EasyBot(Player):

    def winning(self, coordinates: typing.Tuple[typing.List[None], ...], rounds: int):
        clear()
        print_coordinates(coordinates)
        print(f"the winner is {self} in {rounds} rounds")

    def get_move(self,
                 coordinates: typing.Tuple[typing.List[None], typing.List[None], typing.List[None]],
                 error: 'typing.Optional[TicTacToeException]') -> typing.Tuple[int, int]:
        x = round(random() * 2)
        y = round(random() * 2)

        return (x, y)
