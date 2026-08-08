class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}
        for i in range(len(nums)):
            if (nums[i]) in mapp:
                return [mapp[nums[i]], i]
            else:
                mapp[target - nums[i]] = i
