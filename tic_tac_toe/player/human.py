import math
import typing

from tic_tac_toe.abc import Player
from tic_tac_toe.utils import clear

if typing.TYPE_CHECKING:
    from tic_tac_toe import TicTacToeException
    from tic_tac_toe import Board

def print_coordinates(
    board: 'Board'
):
    size= math.sqrt(len(board))
    
    print("+---" * 3 + "+")
    for i, item in enumerate(board):
        print(f"| {item} ", end="")
        if ((i + 1) % size) == 0:
            print("|")
            print("+---" * 3 + "+")


class Human(Player):
    def winning(self, board: 'Board', rounds: int):
        clear()
        print_coordinates(board)
        print(f"the winner is {self} in {rounds} rounds")

    def get_move(
        self,
        coordinates: 'Board',
        error: "typing.Optional[TicTacToeException]",
    ) -> int:
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

            coordinate = input("coordinate: ")
            print("\r", end="")


            print("\r" * 5)
            if coordinate.isdecimal():
                break
            else:
                error_message = "coordinate must be decimal numbers"

        return int(coordinate)
