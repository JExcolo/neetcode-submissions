# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = self.dfs(root)
        return False if result == float("inf") else True
        
    def dfs(self, root):
        if root is None:
            return -1
        
        left = 1 + self.dfs(root.left)
        right = 1 + self.dfs(root.right)

        if right - left > 1 or left - right > 1:
            return float("inf")
        return max(left, right)