# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:
       # BC
        if root is None:
            return False
        
        if root.val==target and root.left is None and root.right is None:
            return True
        
        left = self.hasPathSum(root.left, target- root.val)
        right = self.hasPathSum(root.right, target- root.val)
        return left or right 
        