# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def rec(node, low, high):
            if not node:
                return True

            return low < node.val < high and rec(node.left, low, node.val) and rec(node.right, node.val, high)
            

        return rec(root, float("-inf"), float("inf"))
        