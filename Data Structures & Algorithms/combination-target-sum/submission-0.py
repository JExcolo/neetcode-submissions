class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        holder = set()
        subsets = []

        def dfs(i, targ):
            if targ < 0:
                return
            if i >= len(nums):
                return
            if i < len(nums) and targ == 0:
                if tuple(subsets) not in holder:
                    res.append(subsets[:])
                    holder.add(tuple(subsets))
            subsets.append(nums[i])
            dfs(i, targ - nums[i])

            subsets.pop()
            dfs(i + 1, targ)

        dfs(0, target)
        return res


        
        