# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def traverse(node):
            if not node:
                res.append("N")
                return 
            res.append(str(node.val))
            traverse(node.left)
            traverse(node.right)
            return
        traverse(root)
        res = ",".join(res)
        return res

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        parsed_data = data.split(",")
        vals = iter(parsed_data)
        
        def build():
            cur_val = next(vals)
            if cur_val == "N":
                return None
            else:
                return TreeNode(cur_val, build(), build())
        return build()
        