# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        output = []
        if not pairs:
            return output
        self.add_out(output, pairs)
        for i in range(1, len(pairs)):
            j = i - 1
            while j >= 0 and pairs[j + 1].key < pairs[j].key:
                temp = pairs[j + 1]
                pairs[j + 1] = pairs[j]
                pairs[j] = temp
                j -= 1
            self.add_out(output, pairs)
        
        return output
    def add_out(self, output, pairs):
        first = []
        for pair in pairs:
            first.append(pair)
        output.append(first)