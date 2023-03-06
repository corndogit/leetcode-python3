def generate(numRows: int) -> list[list[int]]:
    if numRows == 1:
        return [[1]]

    if numRows == 2:
        return [[1], [1, 1]]

    rows = [[1], [1, 1]]
    new_row = [1]
    for _ in range(2, numRows):
        for i in range(len(rows[-1]) - 1):
            new_row.append(rows[-1][i] + rows[-1][i + 1])
        new_row.append(1)
        rows.append(new_row)
        new_row = [1]

    return rows


if __name__ == '__main__':
    print(generate(30))
