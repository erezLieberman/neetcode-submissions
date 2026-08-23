# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p:
            return False
        if not q:
            return False
        if not p.right and not p.left and not q.right and not q.left:
            return p.val == q.val
        if (not p.right and q.right) or (not q.right and p.right) or (not q.left and p.left) or (not p.left and q.left):
           return False
        if p.right and q.right and p.right.val != q.right.val or p.left and q.left and p.left.val != q.left.val:
           return False
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
        