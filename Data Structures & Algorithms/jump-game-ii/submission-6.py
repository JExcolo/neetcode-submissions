class Solution:
    def jump(self, nums: List[int]) -> int:

        l, r = 0, 0
        jumps = 0
        while r < len(nums) - 1:
            maxD = 0
            for i in range(l, r + 1):
                maxD = max(maxD, nums[i] + i)
            l = r + 1
            r = maxD
            jumps += 1

        return jumps