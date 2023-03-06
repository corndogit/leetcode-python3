def rotate_1(nums: list[int], k: int) -> None:
    """
    First attempt, uses O(n) space
    """
    n = len(nums)
    offset = k % n
    rotated = [0] * n

    # construct rotated array
    for i in range(0, n):
        rotated[(i + offset) % n] = nums[i]

    # assign to nums
    for j in range(n):
        nums[j] = rotated[j]


def rotate_2(nums: list[int], k: int) -> None:
    """
    Attempt 2 - swapping slices
    """
    n = len(nums)
    k %= n
    if k == 0:
        return

    # swap 0-k with k-n
    nums[n-k:], nums[:n-k] = nums[:n-k], nums[n-k:]


def rotate_3(nums: list[int], k: int) -> None:
    """
    Attempt 3 - pop and insert (very bad with lists, just for fun)
    """
    k %= len(nums)
    if k == 0:
        return

    for _ in range(k):
        nums.insert(0, nums.pop())


if __name__ == '__main__':
    test = list(range(10))
    print(test)
    rotate_2(test, 6)
    print(test)


