class Solution:
    @staticmethod
    def two_sum(numbers: list[int], target: int) -> list[int]:
        # two pointers from start and end
        left = 0
        right = len(numbers) - 1
        while left < right:
            two_sum = numbers[left] + numbers[right]
            if two_sum == target:
                return [left+1, right+1]
            elif two_sum < target:
                left += 1  # makes two sum bigger
            else:
                right -= 1  # makes two sum smaller

        return [-1, -1]  # no answer found


if __name__ == '__main__':
    print(Solution.two_sum([2, 7, 11, 15], 9))
