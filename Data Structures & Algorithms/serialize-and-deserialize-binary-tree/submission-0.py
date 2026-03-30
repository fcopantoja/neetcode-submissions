# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        queue = deque([root])
        result = []

        while queue:
            node = queue.popleft()
            if not node:
                result.append("N")
            else:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        
        return "|".join(result)

            

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        values = data.split("|")
        root = TreeNode(values[0])
        index = 1
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if values[index] != "N":
                node.left = TreeNode(values[index])
                queue.append(node.left)
            
            index += 1

            if values[index] != "N":
                node.right = TreeNode(values[index])
                queue.append(node.right)
            
            index += 1

        return root
        
