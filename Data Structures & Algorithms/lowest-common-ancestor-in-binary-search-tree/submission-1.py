# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def getPath(node, val, built):
            if node.val == val:
                return built + [node]
            if val < node.val:
                return getPath(node.left, val, built + [node])
            else:
                return getPath(node.right, val, built + [node])

        path1 = getPath(root, p.val, [])
        path2 = getPath(root, q.val, [])

        start = min(len(path1), len(path2)) - 1
        while start >= 0:
            if path1[start] == path2[start]:
                return path1[start]
            else:
                start -= 1
                
            

        