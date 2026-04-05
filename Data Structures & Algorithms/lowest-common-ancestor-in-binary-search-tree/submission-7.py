# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def rec(tree, p, q):
            if p.val < tree.val and q.val < tree.val:
                return rec(tree.left, p, q)
            if p.val > tree.val and q.val > tree.val:
                return rec(tree.right, p, q)
            return tree

        return rec(root, p , q) 
        