import random


class MergeSort:
    def _merge(self, arr, left, mid, right):
        """
        Partitions the input array into left and right sub-arrays,
        and then merges them into the original input array.
        """
        # creation of temp sub-arrays and copying data
        n1 = mid - left + 1
        n2 = right - mid

        arr_left = [0] * n1
        arr_right = [0] * n2

        for i in range(n1):
            arr_left[i] = arr[left + i]

        for j in range(n2):
            arr_right[j] = arr[mid + 1 + j]

        idx_left = 0
        idx_right = 0
        idx_merge = left

        # merge using both arrays, then using whatever is left over in either left or right sub-array
        while idx_left < n1 and idx_right < n2:
            if arr_left[idx_left] <= arr_right[idx_right]:
                arr[idx_merge] = arr_left[idx_left]
                idx_left += 1
            else:
                arr[idx_merge] = arr_right[idx_right]
                idx_right += 1
            idx_merge += 1

        while idx_left < n1:
            arr[idx_merge] = arr_left[idx_left]
            idx_left += 1
            idx_merge += 1

        while idx_right < n2:
            arr[idx_merge] = arr_right[idx_right]
            idx_right += 1
            idx_merge += 1

    def merge_sort(self, arr: list, left=None, right=None):
        """
        Sorts an array in-place using merge sort.
        :param arr: the array to sort
        :param left: start index for sub-array
        :param right: end index for sub-array
        """
        if left is None:
            left = 0
        if right is None:
            right = len(arr) - 1
        if left < right:
            mid = left + (right - left) // 2

            self.merge_sort(arr, left, mid)
            self.merge_sort(arr, mid + 1, right)
            self._merge(arr, left, mid, right)


if __name__ == '__main__':
    sorter = MergeSort()
    nums = list(range(25))
    random.shuffle(nums)
    print(f"Sorting this array : {nums}")
    sorter.merge_sort(nums)
    print(f"After merge sort   : {nums}")
