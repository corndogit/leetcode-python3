def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    aux = sorted(nums1 + nums2)
    mid = len(aux) // 2

    if len(aux) % 2 == 0:
        return float(aux[mid] + aux[mid-1]) / 2
    return float(aux[mid])


if __name__ == '__main__':
    print(findMedianSortedArrays([1,3], [2]))
    print(findMedianSortedArrays([1,2], [3,4]))
