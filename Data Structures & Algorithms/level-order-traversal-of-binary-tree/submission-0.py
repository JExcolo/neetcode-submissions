# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue = deque()
        queue.append([root])
        results = [[root.val]]
        while queue:
            nodes = queue.popleft()
            next_lvl = []
            next_vals = []
            for i in range(len(nodes)):
                node = nodes[i]
                if node.left:
                    next_lvl.append(node.left)
                    next_vals.append(node.left.val)
                if node.right:
                    next_lvl.append(node.right)
                    next_vals.append(node.right.val)
            
            if next_lvl:
                queue.append(next_lvl)
                results.append(next_vals)
        
        return results