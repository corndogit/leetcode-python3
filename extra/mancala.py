import random


class Mancala:
    def __init__(self):
        self.players = ("P1", "P2")
        self.board = [[4, 4, 4, 4, 4, 4],
                      [4, 4, 4, 4, 4, 4]]
        self.stores = [0, 0]
        self.player_turn = random.choice(self.players)

    def next_player_turn(self):
        print(f"It is {self.player_turn}'s turn")
        return self.player_turn

    def make_move(self, row, col, player):
        moves = self.board[row][col]
        self.board[row][col] = 0
        pos_x = col
        pos_y = row

        # calculate board moves
        for _ in range(moves):
            if pos_y == 1:  # bottom row
                pos_x += 1
                if pos_x >= len(self.board[1]):
                    if player == "P2":
                        self.stores[1] += 1
                    else:
                        pos_x = len(self.board[1]) - 1
                        self.board[0][pos_x] += 1
                    pos_y = 0
                else:
                    self.board[pos_y][pos_x] += 1
            else:  # top row
                pos_x -= 1
                if pos_x < 0:
                    if player == "P1":
                        self.stores[0] += 1
                    else:
                        pos_x = 0
                        self.board[1][pos_x] += 1
                    pos_y = 1
                else:
                    self.board[pos_y][pos_x] += 1

        # set next player's turn
        if pos_x >= len(self.board[1]) and player == "P2":
            return
        elif pos_x < 0 and player == "P1":
            return
        else:
            self.player_turn = "P1" if self.player_turn == "P2" else "P2"

    def print_board(self):
        print("P1" + " " * 13 + "P2")
        print("  " + " ".join(map(str, self.board[0])) + "   ")
        print(str(self.stores[0]) + " " * 13 + str(self.stores[1]))
        print("  " + " ".join(map(str, self.board[1])) + "   ")
        print()


if __name__ == '__main__':
    game = Mancala()
    next_player = game.next_player_turn()
    game.print_board()
    game.make_move(1, 2, next_player)
    game.print_board()

