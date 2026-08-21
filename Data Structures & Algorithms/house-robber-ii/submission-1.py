class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        one, two = 0, 0
        for i in range(0, len(nums) - 1):
            temp = one
            one = max(nums[i] + two, one)
            two = temp

        res1 = one

        one, two = 0, 0
        for i in range(1, len(nums)):
            temp = one
            one = max(nums[i] + two, one)
            two = temp
        
        res2 = one
        
        return max(res1, res2)
        