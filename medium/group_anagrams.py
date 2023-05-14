from collections import defaultdict
from typing import List


class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        def str_to_key(string: str):
            """Algorithm for producing keys for the anagrams"""
            out = ""
            counter = defaultdict(int)
            for char in string:
                counter[char] += 1

            for k, v in sorted(counter.items()):
                out += f"{k}{v}"
            return out

        anagrams = defaultdict(list)
        for s in strs:
            key = str_to_key(s)
            anagrams[key].append(s)

        return [a for a in anagrams.values()]


if __name__ == '__main__':
    test = ["eat","tea","tan","ate","nat","bat"]
    s = Solution()
    print(s.group_anagrams(test))
