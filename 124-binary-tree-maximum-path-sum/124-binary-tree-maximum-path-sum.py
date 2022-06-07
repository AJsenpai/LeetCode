# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global result
        result = float('-inf')
        self.solve(root)
        return result       
        
    def solve(self, root):        
        global result
        if root is None:
            return 0
        l = self.solve(root.left)
        r = self.solve(root.right)

        temp = max(max(l,r)+root.val, root.val)
        ans = max(temp, l+r+root.val)
        result = max(result, ans)
        return temp
        

        