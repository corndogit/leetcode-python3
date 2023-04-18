def maxLengthBetweenEqualCharacters(s: str) -> int:
    if len(s) < 2:
        return -1
    max_len = -1
    chars_dict = {}

    for idx, char in enumerate(s):
        if char not in chars_dict:
            chars_dict[char] = [idx]
        else:
            chars_dict[char].append(idx)

    for indices in filter(lambda x: len(x) > 1, chars_dict.values()):  # characters occuring at 2 or more indices
        max_len = max(max_len, indices[-1] - indices[0] - 1)

    return max_len


if __name__ == '__main__':
    print("abca", maxLengthBetweenEqualCharacters("abca"))  # 2
    print("aa", maxLengthBetweenEqualCharacters("aa"))  # 0
    print("abc", maxLengthBetweenEqualCharacters("abc"))  # -1
