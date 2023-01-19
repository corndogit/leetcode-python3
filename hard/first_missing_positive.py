class Solution:
    def first_missing_positive(self, nums: list[int]) -> int:
        # remove negatives and 0
        intermediate_set = set(nums)
        missing_int = 1

        # increment missing_int until we reach the first value not in the list
        while missing_int in intermediate_set:
            missing_int += 1

        return missing_int
