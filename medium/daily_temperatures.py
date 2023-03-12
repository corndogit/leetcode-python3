class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        day_diffs = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                popped = stack.pop()
                day_diffs[popped] = i - popped

            stack.append(i)

        return day_diffs
