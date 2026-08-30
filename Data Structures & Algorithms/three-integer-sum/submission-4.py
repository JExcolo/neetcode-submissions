class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        n = len(nums) - 1
        res = []
        def summer(j, l, r):

            while l < r:
                if nums[j] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[j] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    res.append([nums[j], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    r -= 1
                    l += 1
                    
        
        for i in range(n - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            summer(i, i + 1, n)
        
        return res