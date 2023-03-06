def findKthPositive_naive(arr: list[int], k: int) -> int:
    """Naive approach - time complexity: O(n), space complexity: O(n)"""
    arr_set = set(arr)
    missing_stack = []
    missing = 1

    while len(missing_stack) < k:
        if missing not in arr_set:
            missing_stack.append(missing)
        missing += 1

    return missing_stack[-1]


def findKthPositive_bs(arr: list[int], k: int) -> int:
    """Binary search - time complexity: O(n), space complexity: O(1)"""
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] - (mid + 1) < k:
            start = mid + 1
        else:
            end = mid - 1

    return start + k
