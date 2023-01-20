class Solution:
    def find_duplicates(self, nums: list[int]) -> list[int]:
        uniques = set()
        duplicates = set()
        for num in nums:
            if num in uniques:
                duplicates.add(num)
            else:
                uniques.add(num)

        return list(duplicates)


if __name__ == "__main__":
    solution = Solution()
    print(solution.find_duplicates([4, 3, 2, 7, 8, 2, 3, 1]))
