# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()
        if root:
            q.append(root)
            res.append(root.val)
        while q:
            lvl = []
            for i in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                    lvl.append(curr.left.val)
                if curr.right:
                    q.append(curr.right)
                    lvl.append(curr.right.val)
            if lvl:
                res.append(lvl[-1])
        return res
                

        