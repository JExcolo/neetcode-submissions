# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None and val:
            new = TreeNode(val)
            return new
        self.dfs(None, root, val)
        return root

    
    def dfs(self, prev, curr, val):
        if curr is None:
            new = TreeNode(val)
            if prev: 
                if prev.val > new.val:
                    prev.left = new
                else:
                    prev.right = new
            return
        
        if val > curr.val:
            self.dfs(curr, curr.right, val)
        else:
            self.dfs(curr, curr.left, val)
        return
        