# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        
        if not root:
            return output
        
        return self.solve(root,output)
    
    def solve(self, node,output):
        # preorder = root, left, right
        output.append(node.val)
        
        if node.left:
            self.solve(node.left, output)
        if node.right:
            self.solve(node.right, output)
        return output
        
        
        