class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not target in nums:
            return -1

        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        lo = 0
        hi = len(nums)
        mid = (hi + lo) // 2

        while lo < hi and lo + 1 != hi:
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] < target:
                    lo = mid
                else:
                    hi = mid

                mid = (hi + lo) // 2

        if nums[lo] == target:
            return lo