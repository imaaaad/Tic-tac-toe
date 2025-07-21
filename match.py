from table import Table
from option import Option

class Match:
    def __init__(self):
        self.table = Table()
        self.players = [Option('X'), Option('O')]
        self.current = 0

    def play(self):
        print("Welcome to Tic Tac Toe!")
        while True:
            self.table.display()
            player = self.players[self.current]
            print(f"Player {player.symbol}, enter your move (row col): ", end="")
            try:
                row, col = map(int, input().split())
                if not (0 <= row < 3 and 0 <= col < 3):
                    print("[ERROR] Invalid coordinates. Try 0–2 for row/col.")
                    continue
                if not self.table.update(row, col, player.symbol):
                    print("[ERROR] Cell not empty!")
                    continue
            except ValueError:
                print("[ERROR] Please enter two numbers.")
                continue

            if self.table.check_winner(player.symbol):
                self.table.display()
                print(f"🎉 Player {player.symbol} wins!")
                break
            if self.table.is_full():
                self.table.display()
                print("It's a draw!")
                break

            self.current = 1 - self.current
