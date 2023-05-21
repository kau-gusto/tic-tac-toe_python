from random import random
import typing

from tic_tac_toe.datasets import tests
from tic_tac_toe.abc.player import Player
from tic_tac_toe.player.human import print_coordinates
from tic_tac_toe.utils import clear

if typing.TYPE_CHECKING:
    from tic_tac_toe import TicTacToeException
    from tic_tac_toe import ListCoordinatesType
    from tic_tac_toe import CoordinateType


class EasyBot(Player):
    def winning(self, coordinates: "ListCoordinatesType", rounds: int):
        clear()
        print_coordinates(coordinates)
        print(f"the winner is {self} in {rounds} rounds")

    def get_move(
        self,
        coordinates: "ListCoordinatesType",
        _: "typing.Optional[TicTacToeException]",
    ) -> int:
        coordinate = round(random() * len(coordinates))

        return coordinate


class IntermediaryBot(EasyBot):
    def winning(self, coordinates: "ListCoordinatesType", rounds: int):
        clear()
        print_coordinates(coordinates)
        print(f"the winner is {self} in {rounds} rounds")

    def get_move(
        self,
        coordinates: "ListCoordinatesType",
        error: "typing.Optional[TicTacToeException]",
    ) -> int:
        if not error:
            return_coordinate, garante = self.try_winner(coordinates)
            if garante and return_coordinate:
                return return_coordinate
            return_coordinate_defended, garante = self.try_defender(coordinates)
            if garante and return_coordinate_defended:
                return return_coordinate_defended

            if return_coordinate:
                return return_coordinate
            elif return_coordinate_defended:
                return return_coordinate_defended

        return super().get_move(coordinates, error)

    @classmethod
    def _is_other_player(cls, player: Player, coordinate: "CoordinateType"):
        return (not isinstance(coordinate, int)) and coordinate != player

    def try_defender(
        self, coordinates: "ListCoordinatesType"
    ) -> typing.Tuple[typing.Optional[int], bool]:
        return_coordinate: set[int] = set()
        for test in tests:
            a_coordinate, b_coordinate, c_coordinate = test
            a, b, c = (
                coordinates[a_coordinate],
                coordinates[b_coordinate],
                coordinates[c_coordinate],
            )
            if (
                self._is_other_player(self, a)
                or self._is_other_player(self, b)
                or self._is_other_player(self, c)
            ):
                if self._is_other_player(self, a):
                    if self._is_other_player(self, b) and isinstance(c, int):
                        return (c_coordinate, True)
                    if self._is_other_player(self, c) and isinstance(b, int):
                        return (b_coordinate, True)
                    if isinstance(b, int) and isinstance(c, int):
                        return_coordinate.add(b_coordinate)
                        return_coordinate.add(c_coordinate)
                        continue
                if self._is_other_player(self, b):
                    if self._is_other_player(self, c) and isinstance(a, int):
                        return (a_coordinate, True)
                    if isinstance(a, int) and isinstance(c, int):
                        return_coordinate.add(a_coordinate)
                        return_coordinate.add(c_coordinate)
                        continue
                if self._is_other_player(self, c):
                    if isinstance(a, int) and isinstance(b, int):
                        return_coordinate.add(a_coordinate)
                        return_coordinate.add(b_coordinate)

        if len(return_coordinate):
            list_return_coordinate = list(return_coordinate)
            return (
                list_return_coordinate[round(random() * len(return_coordinate)) - 1],
                False,
            )
        return (None, False)

    def try_winner(
        self, coordinates: "ListCoordinatesType"
    ) -> typing.Tuple[typing.Optional[int], bool]:
        return_coordinate: set[int] = set()
        for test in tests:
            a_coordinate, b_coordinate, c_coordinate = test
            a, b, c = (
                coordinates[a_coordinate],
                coordinates[b_coordinate],
                coordinates[c_coordinate],
            )
            if a == self or b == self or c == self:
                if a == self:
                    if b == self and isinstance(c, int):
                        return (c_coordinate, True)
                    if c == self and isinstance(b, int):
                        return (b_coordinate, True)
                    if isinstance(b, int) and isinstance(c, int):
                        return_coordinate.add(b_coordinate)
                        return_coordinate.add(c_coordinate)
                        continue
                if b == self:
                    if c == self and isinstance(a, int):
                        return (a_coordinate, True)
                    if isinstance(a, int) and isinstance(c, int):
                        return_coordinate.add(a_coordinate)
                        return_coordinate.add(c_coordinate)
                        continue
                if c == self:
                    if isinstance(a, int) and isinstance(b, int):
                        return_coordinate.add(a_coordinate)
                        return_coordinate.add(b_coordinate)

        if len(return_coordinate):
            list_return_coordinate = list(return_coordinate)
            return (
                list_return_coordinate[round(random() * len(return_coordinate)) - 1],
                False,
            )
        return (None, False)
