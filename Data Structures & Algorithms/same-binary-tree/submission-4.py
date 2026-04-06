# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def rec(p, q):
            if not p and q:
                return False
            if p and not q:
                return False
            if not p and not q:
                return True
            
            return p.val == q.val and rec(p.left, q.left) and rec(p.right, q.right)

        return rec(p, q)
        