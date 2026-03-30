# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        null_seen = False

        while queue:
            node = queue.popleft()
            if node:
                if null_seen:
                    return False
                queue.append(node.left)
                queue.append(node.right)
            else:
                null_seen = True
        
        return True