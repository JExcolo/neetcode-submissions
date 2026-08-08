class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2 * len(nums)):
            if i >= len(nums):
                j = i - len(nums)
                ans.append(nums[j])
            else:
                ans.append(nums[i])

        return ans