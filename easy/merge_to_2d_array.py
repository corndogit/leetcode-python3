class Solution:
    @staticmethod
    def mergeArrays(nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        table = {}

        def add_values_to_table(nums):
            for k, v in nums:
                if k not in table.keys():
                    table[k] = v
                else:
                    table[k] += v

        add_values_to_table(nums1)
        add_values_to_table(nums2)

        return sorted(table.items())


if __name__ == '__main__':
    n1 = [[1, 2], [2, 3], [4, 5]]
    n2 = [[1, 4], [3, 2], [4, 1]]
    out = Solution.mergeArrays(n1, n2)
    exp = [[1,6],[2,3],[3,2],[4,6]]
    print(out, out == exp)
