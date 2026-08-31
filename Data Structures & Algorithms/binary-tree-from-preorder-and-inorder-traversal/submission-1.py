# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_hm = {}
        preorder_index = 0

        for index, val in enumerate(inorder):
            index_hm[val] = index
        
        def traverse(left, right):
            nonlocal preorder_index
            if left > right :
                return None
            val = preorder[preorder_index]
            preorder_index += 1
            root = TreeNode(val)
            mid = index_hm[val]
            root.left = traverse(left, mid-1)
            root.right = traverse(mid+1, right)
            return root
        
        return traverse(0, len(preorder)-1)
            

    
        