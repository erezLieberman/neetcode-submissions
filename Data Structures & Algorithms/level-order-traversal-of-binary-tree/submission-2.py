# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
      
        dq = deque()
        dq.append(root)
        res = []

        while dq:
            inner_res = []
            level_size = len(dq)
            for i in range(level_size):
                curr = dq.popleft()
                inner_res.append(curr.val)
                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)
            res.append(inner_res)
        return res
                