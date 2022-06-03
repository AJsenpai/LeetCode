# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        # same logic as two sum with hashmap
        def traverse(node):
            if not node:
                return False

            if k - node.val in visited:
                return True
            
            visited.add(node.val)
            
            left = traverse(node.left)
            right = traverse(node.right)
            return left or right
        
        visited = set()
        return traverse(root)
        
        
        