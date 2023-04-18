from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [value[0] for value in Counter(nums).most_common(k)]
