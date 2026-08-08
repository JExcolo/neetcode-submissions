class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        n = len(arr) - 1
        right_max = -1
        for i in range(n, -1, -1):
            current = arr[i]
            arr[i] = right_max
            right_max = max(right_max, current)
        return arr
