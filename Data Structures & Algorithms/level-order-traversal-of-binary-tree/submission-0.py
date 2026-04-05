# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        toReturn = []

        while queue:
            toReturn.append(list(map(lambda x: x.val, queue)))
            toAdd = []
            while queue:
                n = queue.popleft()
                if n.left: toAdd.append(n.left)
                if n.right: toAdd.append(n.right)
            queue = deque(toAdd)

        return toReturn

        