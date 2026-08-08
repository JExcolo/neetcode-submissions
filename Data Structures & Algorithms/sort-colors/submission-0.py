class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        newArray = [0,0,0]
        for i in nums:
            newArray[i] += 1
        
        i = 0
        for j in range(len(newArray)):
            for k in range(0, newArray[j]):
                nums[i] = j
                i += 1
        
        return nums

