# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(p, q):
            if not p and q:
                return False
            if p and not q:
                return False
            if not p and not q:
                return True
            
            return p.val == q.val and same(p.left, q.left) and same(p.right, q.right)
        
        def rec(p, q):
            if not q:
                return True
            if not p:
                return False

            return same(p, q) or rec(p.left, q) or rec(p.right, q)

        return rec(root, subRoot)