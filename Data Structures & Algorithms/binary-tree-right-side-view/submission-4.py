# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        dq = deque([root])

        while dq:
            n = len(dq)
            result.append(dq[-1].val)
            for i in range(n):
                cur = dq.popleft()
                if cur.left:
                    dq.append(cur.left)
                if cur.right:
                    dq.append(cur.right)
        
        return result
        
