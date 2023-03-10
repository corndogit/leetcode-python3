class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        uniques = set()
        longest = 1
        for char in s:
            if char in uniques:
                longest = max(longest, len(uniques))
                uniques = set()
            uniques.add(char)

        return longest


if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLongestSubstring("pwwkew"))
