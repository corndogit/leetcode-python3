def maxSubArray(nums: list[int]) -> int:
    sums = set(nums)
    sums.add(sum(nums))

    for i in range(0, len(nums)):
        for j in range(1, int(len(nums) + 1)):
            sub_nums = nums[i:j]
            if len(sub_nums) > 0:
                sums.add(sum(sub_nums))

    return max(sums)


if __name__ == '__main__':
    # print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(maxSubArray([-2,-1]))
