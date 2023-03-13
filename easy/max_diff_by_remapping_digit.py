class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        uniques = set(s)
        lowest = int(s.replace(s[0], '0'))
        highest = 0

        for i in list(uniques):
            hi_num = s.replace(i, '9')
            highest = max(highest, int(hi_num))

        return highest - lowest
