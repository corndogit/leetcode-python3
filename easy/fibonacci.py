import math


class Solution:
    def fib(self, n: int) -> int:
        # Using Binet's formula
        SQRT_5 = math.sqrt(5)
        a = ((1 + SQRT_5) / 2)**n
        b = ((1 - SQRT_5) / 2)**n
        return int((a - b) / SQRT_5)
