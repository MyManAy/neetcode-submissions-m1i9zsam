# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        def rec(node):
            if not node.left and not node.right:
                return node
            elif not node.left:
                newNode = TreeNode()
                newNode.val = node.val
                newNode.left = rec(node.right)
                newNode.right = None
                return newNode
            elif not node.right:
                newNode = TreeNode()
                newNode.val = node.val
                newNode.right = rec(node.left)
                newNode.left = None
                return newNode
            else:
                newNode = TreeNode()
                newNode.val = node.val
                newNode.left = rec(node.right)
                newNode.right = rec(node.left)
                return newNode

        return rec(root)

        