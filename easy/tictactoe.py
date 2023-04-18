class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        result = None

        def check_row(row_num):
            if sum(grid[row_num]) == 3 or sum(grid[row_num]) == -3:
                return 'A' if sum(grid[row_num]) == 3 else 'B'

        def check_col(col_num):
            column = [val[col_num] for val in grid]
            if sum(column) == 3 or sum(column) == -3:
                return 'A' if sum(column) == 3 else 'B'

        def check_diags():
            diag_top_left = [grid[0][0], grid[1][1], grid[2][2]]
            diag_top_right = [grid[0][2], grid[1][1], grid[2][0]]
            if sum(diag_top_left) == 3 or sum(diag_top_right) == 3:
                return 'A'
            if sum(diag_top_left) == -3 or sum(diag_top_right) == -3:
                return 'B'

        for turn, move in enumerate(moves):
            player_turn = 1 if turn % 2 == 0 else -1  # 1 = A, -1 = B
            row = move[0]
            col = move[1]
            grid[row][col] = player_turn

            # check results
            if result is None:
                result = check_row(row)
            if result is None:
                result = check_col(col)
            if result is None:
                result = check_diags()
            if result is not None:
                break

        if result is None:
            if len(moves) == 9:
                result = "Draw"
            else:
                result = "Pending"

        return result
