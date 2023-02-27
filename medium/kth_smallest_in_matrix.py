class Solution:
    @staticmethod
    def kth_smallest(matrix: list[list[int]], k: int) -> int:
        if len(matrix) == 1 or k == 1:
            return matrix[0][0]

        aux = []
        for row in matrix:
            aux.extend(row)

        aux.sort()
        return aux[k-1]


if __name__ == "__main__":
    print(Solution.kth_smallest([[1,5,9],[10,11,13],[12,13,15]], 8) == 13)
    print(Solution.kth_smallest([[-5]], 1) == -5)
    print(Solution.kth_smallest([[1,2],[1,3]], 2) == 1)
