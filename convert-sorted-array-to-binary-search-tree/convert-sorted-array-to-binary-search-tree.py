# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        
        def buildBST(a,start,end):            
            if start<0 or end>len(a)-1 or start>end:
                return
            mid = start+ ((end-start)//2)
            root = TreeNode(a[mid])
            root.left = self.sortedArrayToBST(a[:mid])
            root.right = self.sortedArrayToBST(a[mid+1:])
            return root
        
        return buildBST(nums,0,len(nums)-1)
        
        