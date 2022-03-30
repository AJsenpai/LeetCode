# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # boundaries
        return self.isBst(root, float('-inf'), float('inf'))
    
    def isBst(self,node,left,right):
        if not node:
            return True
        
        # node level BST property
        if not (node.val > left and node.val<right):
            return False
        
        # Go Left: left boundary remain same and right boundary becomes root/parent
        # Go Right: right boundary remain same and left boundary becomes root/parent
        return self.isBst(node.left, left, node.val) and self.isBst(node.right,node.val, right)
        
        
        
        
        
        
        
        
        