class Solution:
    def rob(self, nums: List[int]) -> int:
        def greed(i, curr, memo):
            if i >= len(nums):
                return curr
            if i in memo:
                return curr + memo[i]
            money = max(greed(i + 1, curr, memo), greed(i + 2, curr + nums[i], memo))
            memo[i] = money
            return money
        
        return greed(0, 0, {})
        

        