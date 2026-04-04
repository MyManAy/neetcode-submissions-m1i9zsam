# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(p, q):
            if not p and q:
                return False
            if not q and p:
                return False
            if not q and not p:
                return True
            else:
                return p.val == q.val and sameTree(p.left, q.left) and sameTree(p.right, q.right)
        
        def rec(roo, subRoo):
            if not roo:
                return False
            if sameTree(roo, subRoo):
                return True
            
            return rec(roo.left, subRoo) or rec(roo.right, subRoo)
            
        return rec(root, subRoot)