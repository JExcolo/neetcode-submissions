class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)
        dp[0], dp[1] = cost[0], cost[1]

        for i in range(2, len(cost) + 1):
            if i < len(cost):
                dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
            else:
                dp[i] = min(dp[i - 1], dp[i - 2])
        
        return dp[-1]