# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return False if self.dfs(root) == float("inf") else True
        
    def dfs(self, root):
        if root is None:
            return -1
        
        left = 1 + self.dfs(root.left)
        right = 1 + self.dfs(root.right)

        if abs(right - left) > 1:
            return float("inf")
        return max(left, right)