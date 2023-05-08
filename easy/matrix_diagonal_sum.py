def diagonal_sum(mat: list[list[int]]) -> int:
    n = len(mat)
    mid = n // 2
    val = 0
    for i in range(mid):
        val += sum((mat[i][i],                # top left
                    mat[n - i - 1][i],        # bottom left
                    mat[i][-1 - i],           # top right
                    mat[n - i - 1][-1 - i]))  # bottom right

    if n % 2 != 0:
        val += mat[mid][mid]  # add missing centre value

    return val


if __name__ == '__main__':
    cases = {
        25: [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]],
        8: [[1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]],
        5: [[5]],
        55: [[7, 3, 1, 9],
             [3, 4, 6, 9],
             [6, 9, 6, 6],
             [9, 5, 8, 5]]
    }
    passed = 0
    for k, v in cases.items():
        res = diagonal_sum(v)
        if k == res:
            print("Passed")
            passed += 1
        else:
            print(f"Failed - expected {k}, got {res}")
    print(f"Passed {passed}/{len(cases)} test cases.")
