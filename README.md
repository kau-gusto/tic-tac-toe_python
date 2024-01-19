# tic-tac-toe em Python

`Uma simples biblioteca para a criação do jogo de tabuleiro TIC TAC TOE`

## tic_tac_toe

Esse é um exemplo de como pode ser organizada a lógica do jogo

```python
# .../main.py
from tic_tac_toe import TicTacToe, TicTacToeException
from tic_tac_toe.player.bot import EasyBot
from tic_tac_toe.player.human import Human, print_coordinates
from tic_tac_toe.utils import clear


if __name__ == "__main__":
    tic_tac_toe = TicTacToe(Human("X"), EasyBot("O"))
    while True:
        try:
            tic_tac_toe.play()
        except TicTacToeException as exc:
            clear()
            print_coordinates(tic_tac_toe.board)
            print(exc)
        if input("Do you want to continue?(y, n)\n") != "y":
            break


```

Para executar, insira o seguinte comando no terminal

```python main.py```

## tic_tac_toe.abc

Módulos para abstração de classes padrões para o funcionamento do Jogo

### Player(char:str)

```python
from random import random
from tic_tac_toe.abc import Player

if typing.TYPE_CHECKING:
    from tic_tac_toe import TicTacToeException
    from tic_tac_toe import Board


class Human(Player):
    def winning(
        self,
        coordinates: 'Board',
        rounds: int,
    ):
        print("Wow")

    def get_move(
        self,
        coordinates: 'Board',
        error: "typing.Optional[TicTacToeException]",
    ) -> int:
        return round(random() * len(coordinates))
```

## tic_tac_toe.board

### tic_tac_toe.board.Board()

exemplo:

```python
board = Board()

board.make_move(player, 0..8)
#...

winner = Board.test_winner(board.board)
# ou
winner = board.get_winner()
```

#### make_move(player: Player, coordinate: int) -> None

È a forma onde as coordenadas são ocupadas e assim são feitos os movimentos no tabuleiro, porém é aqui que os erros são ocasionados

#### Board.test_winner(board: tic_tac_toe.board.ListBoardType) -> Optional[Player]

Caso haja algum vencedor é retornado o mesmo, se não o retorno é nulo

`O método é estático para caso o player tenha que fazer alguma previsão`

#### get_winner() -> Optional[Player]

Caso haja algum vencedor é retornado o mesmo, se não o retorno é nulo

### tic_tac_toe.board.TicTacToeException(Exception)

A base para todas as exceções do tabuleiro

### tic_tac_toe.board.TieTicTacToe(TicTacToeException)

Ocorre quando todos as coordenadas do tabuleiro estão ocupadas, porém não há um vencedor

```python
board.make_move(player, n)
# 9 vezes ...
board.get_winner() # raise TieTicTacToeException
```

### tic_tac_toe.board.CoordinateExceededException(TicTacToeException)

Ocorre quando é feito um movimento em que a coordenadas não existe no tabuleiro

```python
board.make_move(player, n) # raise CoordinateExceededTicTacToeException
```

### tic_tac_toe.board.JustPlayedException(TicTacToeException)

Ocorre quando um jogador tenta jogador duas vezes seguidas

```python
board.make_move(player, n)
board.make_move(player, n + 1) # raise JustPlayedTicTacToeException
```

### tic_tac_toe.board.CoordinateOccupiedException(TicTacToeException)

Ocorre quando a coordenada do tabuleiro a ser feito o movimento já estar ocupada

```python
board.make_move(player, n)
board.make_move(other_player, n) # raise CoordinateOccupiedTicTacToeException
```

## tic_tac_toe.player

### human.Human(char:str)

Os movimentos são pedidos por cli, repetindo o pedido caso haja algum erro

```python
from tic_tac_toe.player.human import Human, print_coordinates

if __name__ == "__main__":
    tic_tac_toe = TicTacToe(Human("X"), Human("O"))
    #...
```

### human.print_coordinates(board:tic_tac_toe.board.Board)

Serve para facilitar a visualização do usuário para caso haja alguma exceção

```python
try:
    game.play() # raise TicTacToeException
except TicTacToeException as exc:
    print_coordinates(game.board)
    print(exc)
```

### bot.EasyBot(char:str)

Os movimentos desse bot são totalmente aleatórios, nem mesmo se baseando em coordenadas já ocupadas

```python
from tic_tac_toe.player.bot import EasyBot
from tic_tac_toe.player.human import Human, print_coordinates

if __name__ == "__main__":
    tic_tac_toe = TicTacToe(Human("X"), EasyBot("O"))
    #...
```

### bot.IntermediaryBot(char:str)

Os movimentos desse bot se baseiam em coordenadas já ocupadas, ocupando aquelas que ajude-o a fazer uma linha ou limite a jogada do oponente, porem não usando nenhuma estrategia para adiantar o jogo

```python
from tic_tac_toe.player.bot import IntermediaryBot
from tic_tac_toe.player.human import Human, print_coordinates

if __name__ == "__main__":
    tic_tac_toe = TicTacToe(Human("X"), IntermediaryBot("O"))
    #...
```

## tic_tac_toe.utils

### clear

Serve para facilitar a limpeza da visão do usuário caso necessário

```python
try:
    game.play() # raise TicTacToeException
except TicTacToeException as exc:
    clear()
    print_coordinates(game.board)
    print(exc)
```
