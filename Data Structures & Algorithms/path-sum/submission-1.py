# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
            
        paths = []
        stack = []
        stack.append((root, [root.val]))
        visited = set()

        while stack:
            curr, path = stack.pop()

            if not curr.left and not curr.right:
                paths.append((curr, path))
                if sum(path) == targetSum:
                    return True
            
            if curr.left:
                stack.append((curr.left, path + [curr.left.val]))
            
            if curr.right:
                stack.append((curr.right, path + [curr.right.val]))
        

        return False


            