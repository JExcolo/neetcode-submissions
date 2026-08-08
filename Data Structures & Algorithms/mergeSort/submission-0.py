# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeHelper(pairs, 0, len(pairs) - 1)

    def mergeHelper(self, pairs, start, end):
        if end -  start + 1 <= 1:
                 return pairs
            
        m = (start + end) // 2
        self.mergeHelper(pairs, start, m)
        self.mergeHelper(pairs, m + 1, end)
        self.merge(pairs, start, m, end)

        return pairs

    def merge(self, arr, s, m, e):
        leftArr = arr[s: m + 1]
        rightArr = arr[m + 1: e + 1]
        i, j, k = 0, 0, s
        while(i < len(leftArr) and j < len(rightArr)):
            if leftArr[i].key <= rightArr[j].key:
                arr[k] = leftArr[i]
                i += 1
            else:
                arr[k] = rightArr[j]
                j += 1
            k += 1
        while(i < len(leftArr)):
            arr[k] = leftArr[i]
            i += 1
            k += 1
            
        while(j < len(rightArr)):
            arr[k] = rightArr[j]
            j += 1
            k += 1

        # def merge(list1, list2):
        #     newList = []
        #     newP, leftP, rightP = 0, 0, 0

        #     while(leftP <= len(list1) and rightP <= len(list2)):
        #         if list1[leftP] > list2[rightP]:
        #             newList[newP].append(list2[rightP])
        #             rightP++
        #         else:
        #             newList[newP].append(list1[leftP])
        #             leftP++

        #     if leftP < len(list1) - 1:
        #         for obj in list1:
        #             newList.append(obj)
            
        #     if rightP < len(list2) - 1:
        #         for obj in list2:
        #             newList.append(obj)
