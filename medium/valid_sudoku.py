from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_subgrid(row_idx, col_idx) -> bool:
            """Check a grid given the coords of its top left square"""
            nums = set()
            for y in range(row_idx, row_idx + 3):
                for x in range(col_idx, col_idx + 3):
                    if board[y][x] in nums and board[y][x] != ".":
                        return False
                    nums.add(board[y][x])
            return True

        def check_line(line: list):
            """Check a given row or column list"""
            nums = set()
            for char in line:
                if char in nums and char != ".":
                    return False
                nums.add(char)
            return True

        # check subgrids
        for corner_row in range(0, 9, 3):
            for corner_col in range(0, 9, 3):
                if not check_subgrid(corner_row, corner_col):
                    return False

        # check rows
        for row in board:
            if not check_line(row):
                return False

        # check cols
        for i in range(len(board)):
            col = [board[j][i] for j in range(len(board))]
            if not check_line(col):
                return False

        return True


if __name__ == '__main__':
    solution = Solution()
    tests = [([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]], True),
             ([["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]], False),
             ([[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]], False),
             ([[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]], True)]

    for id, test in enumerate(tests):
        output = solution.isValidSudoku(test[0])
        result = "passed" if output == test[1] else "FAILED"
        print(f"Test #{id} {result}")
