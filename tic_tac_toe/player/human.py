import typing

from tic_tac_toe.abc.player import Player
from tic_tac_toe.utils import clear

if typing.TYPE_CHECKING:
    from tic_tac_toe import TicTacToeException


def print_coordinates(
    coordinates: typing.Tuple[typing.List[None], typing.List[None], typing.List[None]]
):
    print(" " * 3, end="x")
    for i in range(3):
        print(f"{i}", end=" " * 3)
    print("\ny", "+---" * 3 + "+")
    for i, line in enumerate(coordinates):
        print(f"{i} ", end="")
        for item in line:
            print(f"| {item if item else ' '} ", end="")
        print("|")
        print(" ", "+---" * 3 + "+")


class Human(Player):
    def winning(self, coordinates: typing.Tuple[typing.List[None], ...], rounds: int):
        clear()
        print_coordinates(coordinates)
        print(f"the winner is {self} in {rounds} rounds")

    def get_move(
        self,
        coordinates: typing.Tuple[typing.List[None], ...],
        error: "typing.Optional[TicTacToeException]",
    ) -> typing.Tuple[int, int]:
        error_message = None
        while True:
            clear()
            if error:
                error_message = error.args[0]
            if error_message:
                print(error_message)
                error_message = None
                error = None
            print_coordinates(coordinates)

            print(f"player -> {self.char}\r")
            print()

            x = input("x: ")
            print("\r", end="")
            y = input("y: ")
            print("\r", end="")

            print("\r" * 5)
            if x.isdecimal() and y.isdecimal():
                break
            else:
                error_message = "x and y must be decimal numbers"

        return (int(x), int(y))
