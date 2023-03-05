class Solution:
    def __init__(self, bad_version: int):
        self.bad_version = bad_version

    def isBadVersion(self, version: int) -> bool:
        return version == self.bad_version

    def firstBadVersion(self, n: int) -> int:
        if self.isBadVersion(1):
            return 1

        lo = 1
        hi = n
        mid = n // 2

        while lo + 1 < hi:
            if self.isBadVersion(mid):
                hi = mid
            else:
                lo = mid

            mid = (lo + hi) // 2

        return hi


if __name__ == "__main__":
    print(Solution(4).firstBadVersion(5))
    print(Solution(2126753390).firstBadVersion(1702766719))
    print(Solution(1).firstBadVersion(1))
