# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {inorder[i]: i for i in range(len(inorder))}

        def rec(pl, pr, il, ir):
            if pl > pr or il > ir:
                return None

            val = preorder[pl]
            node = TreeNode(val)
            i = inorder_map[val]

            preorder_len = i - il
            node.left = rec(pl + 1, pl + preorder_len, il, i - 1)
            node.right = rec(pl + preorder_len + 1, pr, i + 1, ir)
            return node

        return rec(0, len(preorder) - 1, 0, len(inorder) - 1)
        