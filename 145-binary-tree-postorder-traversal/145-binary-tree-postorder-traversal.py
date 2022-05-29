# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        if not root:
            return output
        
        return self.solve(root,output)
    
    def solve(self,node,output):
        # postorder - left,right,root
        if node.left:
            self.solve(node.left,output)
        
        if node.right:
            self.solve(node.right,output)
        
        output.append(node.val)
        
        return output