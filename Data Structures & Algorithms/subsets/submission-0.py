class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = []
        subsets = []
        def subber(i):
            if i >= len(nums):
                arr.append(subsets[:])
                return
            subsets.append(nums[i])
            subber(i + 1)

            subsets.pop()
            subber(i + 1)
        
        subber(0)
        return arr





        