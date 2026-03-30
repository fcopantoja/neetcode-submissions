# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        queue = deque([root])
        result = 0
        while queue:
            node = queue.popleft()
            if not node:
                continue

            if low <= node.val <= high:
                result += node.val
            
            if node.val >= low:
                queue.append(node.left)
            
            if node.val <= high:
                queue.append(node.right)


        return result