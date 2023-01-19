class Solution:
    def twosum(self, nums: list[int], target: int) -> list[int]:
        # create empty dict
        nums_dict = {}

        for i in range(len(nums)):
            # use result of target - nums[i] as key to find index of result
            if target - nums[i] in nums_dict:
                return [nums_dict[target - nums[i]], i]

            # add index with its value as the key to a dict for faster lookups later
            nums_dict[nums[i]] = i
