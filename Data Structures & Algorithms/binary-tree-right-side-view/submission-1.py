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
        lvls = []
        q = deque()
        if root:
            q.append(root)
            lvls.append([root.val])
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
                lvls.append(lvl)
        # print(lvls)
        if lvls:
            for lev in lvls:
                res.append(lev[-1])
        
        return res
                

        