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
        level = 0

        while queue:
            result.append([])
            for i in range(len(queue)):
                curr = queue.popleft()
                result[level].append(curr.val)
                
                if curr.right:
                    queue.append(curr.right)
                
                if curr.left:
                    queue.append(curr.left)

            if level % 2 == 0:
                result[level] = reversed(result[level])
            level += 1
        
        return result
