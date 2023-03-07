class Solution:
    @staticmethod
    def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        n1 = nums1[:m]
        n2 = nums2[:n]

        for i in range(len(nums1) - 1, -1, -1):
            if len(n1) > 0 and len(n2) > 0:
                if n1[-1] > n2[-1]:
                    nums1[i] = n1.pop()
                else:
                    nums1[i] = n2.pop()

            elif len(n1) > 0:
                nums1[i] = n1.pop()

            elif len(n2) > 0:
                nums1[i] = n2.pop()
