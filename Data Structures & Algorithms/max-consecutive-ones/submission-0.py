class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        curr_ones = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr_ones += 1
            else:
                max_ones = max(max_ones, curr_ones)
                curr_ones = 0

        
        max_ones = max(max_ones, curr_ones)
        return max_ones