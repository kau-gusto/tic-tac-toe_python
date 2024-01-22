def main():
    import math
    import typing

    from rich.console import Console
    from rich.table import Table
    from rich.prompt import Prompt
    from rich.layout import Layout
    from rich.live import Live



    from .game import TicTacToe, TicTacToeException
    from .player.ia import IntermediaryBot
    from .player.human import Human

    if typing.TYPE_CHECKING:
        from .board import Board

    layout = Layout(size=16)
    layout.add_split(Layout(name="table"))
    layout.add_split(Layout(name="player"))
    layout.add_split(Layout(name="coordinates"))
    layout.add_split(Layout(name="winner"))



    prompt = Prompt()
    console = Console()

    def update_table_coordinates(board: "Board"):
        table = Table(title="Tic Tac Toe", show_header=False, show_lines=True)
        size = int(math.sqrt(len(board)))

        for index in range(size):
            initial_index = index * size
            table.add_row(
                *map(
                    lambda cell: str(cell),
                    board.board[initial_index : initial_index + size],
                )
            )
        layout["table"].update(table)
        #console.print(layout)

    def get_move(human, coordinates: "Board", error):
        error_message = None
        if error:
            error_message = error.args[0]
        while True:
            if error_message:
                console.print(error_message, style="yellow")
                error_message = None
                error = None
            update_table_coordinates(coordinates)
            """ console.print(
                f"[i]player[/i] [b blink]->[/] [blue on white b]{human.char}[/]"
            ) """
            layout["player"].update(f"[i]player[/i] [b blink]->[/] [blue on white b]{human.char}[/]")
            layout["coordinates"].update("coordinate")
            coordinate = input()
            #console.clear()
            if coordinate.isdecimal():
                break
            else:
                error_message = "coordinate must be decimal numbers"

        return int(coordinate)

    tic_tac_toe = TicTacToe(Human("X", get_move), IntermediaryBot("O"))

    with Live(layout, auto_refresh=False) as live:
    
        try:
            #console.print(layout)
            winner = tic_tac_toe.play()
            #console.clear()
            update_table_coordinates(tic_tac_toe.board)
            layout["winner"].update(f"the winner is [b]{winner}[/b] in {tic_tac_toe.rounds} rounds")
            """ console.print(
                f"the winner is [b]{winner}[/b] in {tic_tac_toe.rounds} rounds"
            ) """
        except TicTacToeException as exc:
            console.clear()
            update_table_coordinates(tic_tac_toe.board)
            console.print(exc)
        if (
            prompt.ask("Do you want to continue?", choices=["y", "n"], default="y")
            != "y"
        ):
            live.stop()


if __name__ == "__main__":
    main()
