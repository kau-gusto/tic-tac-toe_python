from random import random
import typing

from tic_tac_toe.abc.player import Player
from tic_tac_toe.player.human import print_coordinates
from tic_tac_toe.utils import clear

if typing.TYPE_CHECKING:
    from tic_tac_toe import TicTacToeException
    from tic_tac_toe import ListCoordinatesType


class EasyBot(Player):
    def winning(self, coordinates: 'ListCoordinatesType', rounds: int):
        clear()
        print_coordinates(coordinates)
        print(f"the winner is {self} in {rounds} rounds")

    def get_move(
        self,
        coordinates: 'ListCoordinatesType',
        _: "typing.Optional[TicTacToeException]",
    ) -> int:
        coordinate = round(random() * len(coordinates))

        return coordinate
