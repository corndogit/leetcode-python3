class Solution:
    def tribonacci(self, n: int) -> int:
        # iterative with DP
        res = {0: 0, 1: 1, 2: 1}

        if n in res:
            return res[n]

        for i in range(3, n + 1):
            res[i] = res[i - 1] + res[i - 2] + res[i - 3]

        return res[n]
