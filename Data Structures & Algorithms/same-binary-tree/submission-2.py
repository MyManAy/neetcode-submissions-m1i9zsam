# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def rec(n1, n2):
            if not n1 and n2:
                return False
            elif n1 and not n2:
                return False
            elif not n1 and not n2:
                return True
            else:
                return n1.val == n2.val and rec(n1.left, n2.left) and rec(n1.right, n2.right)

        return rec(p, q)

        