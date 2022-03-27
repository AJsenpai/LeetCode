# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:        
        self.result = float('-inf')
        
        def getDiameter(root):
            if root is None:
                return 0
            
            left = getDiameter(root.left)
            right = getDiameter(root.right)
            
            temp = max(left,right) + 1  # if current node is not ans
            ans = max(temp, 1+left+right) # if current node is ans
            
            self.result = max(self.result, ans) 
            return temp
        
        getDiameter(root)
        return self.result-1 # asking for edges
        
        
        
        
        