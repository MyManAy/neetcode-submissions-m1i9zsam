# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        i_map = {inorder[i]: i for i in range(len(inorder))}
        def rec(pl, pr, il, ir):
            if pr < pl or ir < il:
                return None

            val = preorder[pl]
            node = TreeNode(val)
            i = i_map[val]

            left_size = i - il

            node.left = rec(pl + 1, pl + left_size, il, i - 1)
            node.right = rec(pl + left_size + 1, pr, i + 1, ir)

            return node

        return rec(0, len(preorder) - 1, 0, len(inorder) - 1)

        