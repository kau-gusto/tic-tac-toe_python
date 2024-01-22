from random import random
import typing

from ..datasets import TESTS
from ..abc import Player
from ..board import Board

if typing.TYPE_CHECKING:
    from ..game import TicTacToeException
    from ..board import Board, ItemType


class EasyBot(Player):
    def get_move(
        self,
        board: "Board",
        _: "typing.Optional[TicTacToeException]",
    ) -> int:
        coordinate = round(random() * len(board))

        return coordinate


class IntermediaryBot(EasyBot):
    def get_move(
        self,
        board: "Board",
        error: "typing.Optional[TicTacToeException]",
    ) -> int:
        other_players:set[Player] = set()
        if not error:
            for index, cell in enumerate(board):
                test = list(board.board)

                if isinstance(cell, int):
                    test[index] = self
                    if not Board.test_winner(test) is None:
                        return index
                    else:
                        for player in list(other_players):
                            test[index] = player
                            if not Board.test_winner(test) is None:
                                return index
                elif not cell is None and self._is_other_player(self, cell):
                    other_players.add(cell) # type: ignore
                

        return super().get_move(board, error)

    @classmethod
    def _is_other_player(cls, player: Player, coordinate: "ItemType"):
        return coordinate != player
