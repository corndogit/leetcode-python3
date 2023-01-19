class Solution:
    def int_to_roman(self, num: int) -> str:
        romans = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I',
        }

        keys = sorted(romans.keys())
        intermediate = num
        romanized = ""

        while len(keys) > 0:
            if keys[-1] > intermediate:
                keys.pop(-1)
            elif keys[-1] == intermediate:
                romanized += romans[keys.pop(-1)]
                return romanized
            else:
                romanized += romans[keys[-1]]
                intermediate -= keys[-1]
        return romanized


if __name__ == "__main__":
    solution = Solution()
    print(solution.int_to_roman(3), "Pass" if solution.int_to_roman(3) == "III" else "Fail")
    print(solution.int_to_roman(58), "Pass" if solution.int_to_roman(58) == "LVIII" else "Fail")
    print(solution.int_to_roman(1994), "Pass" if solution.int_to_roman(1994) == "MCMXCIV" else "Fail")
