# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = []
        
        queue.append(root)

        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.pop()
                print(node.val)
                var = node.left
                node.left = node.right
                node.right = var
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            
        return root
