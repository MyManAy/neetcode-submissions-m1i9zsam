# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def rec(p, q):
            if p and not q:
                return False
            if q and not p:
                return False
            elif not q and not p:
                return True
            else:
                return q.val == p.val and rec(p.left, q.left) and rec(p.right, q.right)

        return rec(p, q)
