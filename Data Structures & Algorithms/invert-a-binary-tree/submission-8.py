# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def rec(node):
            if not node:
                return None
            temp = node.left
            node.left = rec(node.right)
            node.right = rec(temp)
            return node

        return rec(root)