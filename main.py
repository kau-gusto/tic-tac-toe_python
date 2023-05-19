
from tic_tac_toe import TicTacToe, TicTacToeException
from tic_tac_toe.player.bot import EasyBot
from tic_tac_toe.player.human import Human, print_coordinates
from tic_tac_toe.utils import clear


def main():
    tic_tac_toe = TicTacToe(Human("X"), EasyBot("O"))
    while True:
        try:
            tic_tac_toe.play()
        except TicTacToeException as exc:
            clear()
            print_coordinates(tic_tac_toe.coordinates)
            print(exc)
        if input("Do you want to continue?(y, n)\n") != "y":
            break


if __name__ == "__main__":
    main()
