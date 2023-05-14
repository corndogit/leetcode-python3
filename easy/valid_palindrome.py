class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = ""
        for char in s:
            if char.isalpha():
                stripped += char.lower()
            elif char.isnumeric():
                stripped += char
        return stripped == stripped[::-1]


if __name__ == '__main__':
    test = "A man, a plan, a canal: Panama"
    solver = Solution()
    print(solver.isPalindrome(test))
