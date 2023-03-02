import itertools

class Solution:
    @staticmethod
    def compress(chars: list[str]):
        if len(chars) == 1:
            return len(chars)

        compressed = []
        for unique, group in itertools.groupby(chars):
            compressed.append(unique)
            count = len(list(group))
            if count > 1:
                for char in str(count):
                    compressed.append(char)

        end = len(compressed)
        for i in range(end):
            chars[i] = compressed[i]
        del chars[end:]
        return len(chars)


if __name__ == "__main__":
    test_case = ["a","a","b","b","c","c","c"]
    print(Solution.compress(test_case))
