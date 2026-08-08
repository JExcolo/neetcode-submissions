class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[i + m] = nums2[i]
        
        self.mergeSort(nums1, 0, m + n - 1)
    
    def mergeSort(self, arr, s, e):
        if e - s + 1 <= 1:
            return arr
        
        m = (e + s) // 2

        self.mergeSort(arr, s, m)
        self.mergeSort(arr, m + 1, e)

        self.merging(arr, s, m, e)


    def merging(self, arr, s, m, e):
        i, j, k = 0, 0, s
        left = arr[ s: m + 1]
        right = arr[ m + 1: e + 1 ]
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


