class Table:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def display(self):
        print("\nCurrent Board:")
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def update(self, row, col, symbol):
        if self.board[row][col] == ' ':
            self.board[row][col] = symbol
            return True
        return False

    def is_full(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def check_winner(self, symbol):
        b = self.board
        return any([
            all(b[i][j] == symbol for j in range(3)) for i in range(3)
        ]) or any([
            all(b[i][j] == symbol for i in range(3)) for j in range(3)
        ]) or all([
            b[i][i] == symbol for i in range(3)
        ]) or all([
            b[i][2 - i] == symbol for i in range(3)
        ])
