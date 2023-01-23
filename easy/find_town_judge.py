class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if n == 1:
            return n

        trust_dict = {person: set() for person in range(1, n+1)}
        for t in trust:
            trust_dict[t[0]].add(t[1])

        empty_keys = list(filter(lambda x: not trust_dict[x], trust_dict))
        if len(empty_keys) != 1:
            return -1
        for k, v in trust_dict.items():
            if empty_keys[0] not in v and k != empty_keys[0]:
                return -1
        return empty_keys[0]
