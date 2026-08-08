# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.qshelper(pairs, 0, len(pairs) - 1)
        return pairs

    
    def qshelper(self, arr, s, e):
        if e - s + 1 <= 1:
            return
        
        pivot = arr[e]
        left = s

        for i in range(s, e):
            if arr[i].key < pivot.key:
                arr[i], arr[left] = arr[left], arr[i]
                left += 1

        arr[e], arr[left] = arr[left], arr[e]

        self.qshelper(arr, s, left - 1)
        self.qshelper(arr, left + 1, e)

        