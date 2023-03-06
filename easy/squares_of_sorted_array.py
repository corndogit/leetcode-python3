def sortedSquares(nums: list[int]) -> list[int]:
    return sorted(map(lambda n: n*n, nums))


if __name__ == '__main__':
    inputs = (  # input, output
        ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
        ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121])
    )

    for i in inputs:
        print(f"Input: {i[0]}\nOutput: {sortedSquares(i[0])}\nExpected: {i[1]}")
        print('-' * 20)
