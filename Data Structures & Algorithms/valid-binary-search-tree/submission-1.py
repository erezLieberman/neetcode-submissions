# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def validate(self, node, min_bound, max_bound):
            if not node:
                return True

            if min_bound >= node.val or max_bound <= node.val:
                return False

            return self.validate(node.left, min_bound, node.val) and self.validate(node.right, node.val, max_bound)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:   
        return self.validate(root, float("-inf"), float("inf"))
