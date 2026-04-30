# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBSTDFS(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0

            value = node.val if low <= node.val <= high else 0
            value += dfs(node.left)
            value += dfs(node.right)

            return value
    
        return dfs(root)

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]
        res = 0

        while stack:
            node = stack.pop()

            if low <= node.val <= high:
                res += node.val
        
            if node.left and node.val >= low:
                stack.append(node.left)
            
            if node.right and node.val <= high:
                stack.append(node.right)

        return res

