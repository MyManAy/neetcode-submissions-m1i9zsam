# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def gethash(node):
            if not node:
                return "#"

            lhash = gethash(node.left)
            rhash = gethash(node.right)

            newhash = f"({lhash}){node.val}({rhash})"

            return newhash
        
        subhash = gethash(subRoot)

        def rec(node): 
            nonlocal subhash
            if gethash(node) == subhash:
                return True

            if not node:
                return False

            return rec(node.left) or rec(node.right)

        return rec(root)