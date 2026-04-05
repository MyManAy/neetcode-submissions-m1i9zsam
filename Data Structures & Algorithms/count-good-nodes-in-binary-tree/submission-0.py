# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def rec(largest, node):
            if not node:
                return
            nonlocal res
            if node.val >= largest:
                res += 1

            largest = max(largest, node.val)
            rec(largest, node.left)
            rec(largest, node.right)

        rec(float("-inf"), root)
        return res
        