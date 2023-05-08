import random


class Mancala:
    def __init__(self, stones_per_hole: int):
        # instance variables (AKA fields)
        self.players = ("P1", "P2")
        self.board = [[stones_per_hole] * 6 for _ in range(2)]  # a 6x2 array with n number of stones in each "hole"
        self.stores = [0, 0]
        self.player_turn = random.choice(self.players)
        self.is_won = False
        self.winner = None

    def _next_player_turn(self):
        """Prints the next player's turn and returns the value"""
        print(f"It is {self.player_turn}'s turn")
        return self.player_turn

    def _make_move(self, row, col, player):
        """Calculate the move given its position on the board and the player that made it"""
        # validate move
        correct_row = (player == "P1" and row == 0) or (player == "P2" and row == 1)
        out_of_bounds = col < 0 or col >= len(self.board[1])
        empty_hole = False
        if not out_of_bounds:
            empty_hole = self.board[row][col] == 0
        if out_of_bounds or empty_hole or not correct_row:
            print("Invalid selection, try again")
            return

        # take stones from the selected hole
        moves = self.board[row][col]
        self.board[row][col] = 0

        # calculate board moves
        pos_x = col
        pos_y = row
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

        # check for win
        winner = self._check_for_game_end()
        if winner:
            if winner == "tie":
                print("The result is a tie!")
            else:
                print(f"{winner} wins!")
            self.print_board()
            self.is_won = True
            return

        # set next player's turn
        if pos_x >= len(self.board[1]) and player == "P2":  # P2 gets a repeat
            print("Bonus turn!")
            return
        elif pos_x < 0 and player == "P1":  # P1 gets a repeat
            print("Bonus turn!")
            return
        else:
            self.player_turn = "P1" if self.player_turn == "P2" else "P2"  # switch players

    def print_board(self):
        """Pretty-prints the game board"""
        print("P1" + " " * 13 + "P2")
        print("  " + " ".join(map(str, self.board[0])) + "   ")
        print(str(self.stores[0]) + " " * 13 + str(self.stores[1]))
        print("  " + " ".join(map(str, self.board[1])) + "   ")
        print()

    def _check_for_game_end(self):
        """Checks if either of the sides of the board are empty, giving the remaining pieces to whichever player made
        the last move."""
        board_sums = (sum(self.board[0]), sum(self.board[1]))
        if board_sums[0] == 0 or board_sums[1] == 0:
            if board_sums[0] == 0:  # P1 gets remaining stones
                self.stores[0] += board_sums[1]
            else:
                self.stores[1] += board_sums[0]

            if self.stores[0] > self.stores[1]:
                return "P1"
            if self.stores[0] < self.stores[1]:
                return "P2"
            if self.stores[0] == self.stores[1]:
                return "tie"
        else:
            return None

    def start(self):
        """Begins a game of Mancala"""
        while not self.is_won:
            next_player = self._next_player_turn()
            self.print_board()
            print(f"{next_player}'s turn, enter the hole number from 1-6")
            select = int(input()) - 1
            self._make_move(0 if next_player == "P1" else 1, select, next_player)


if __name__ == '__main__':
    game = Mancala(4)
    game.start()
