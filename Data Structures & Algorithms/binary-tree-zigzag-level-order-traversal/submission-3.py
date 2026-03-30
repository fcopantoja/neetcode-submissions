# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level = []
            for i in range(len(queue)):
                curr = queue.popleft()
                level.append(curr.val)
                if curr.right:
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)

            if len(result) % 2 == 0:
                level.reverse()
            result.append(level)
        
        return result
