# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        return self.solve(root.left,root.right)
    
    def solve(self,left,right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        
        if left.val ==right.val:
            outPair = self.solve(left.left, right.right)
            inPair = self.solve(left.right, right.left)
            return outPair and inPair
        else:
            return False
    
        # mimicing recursion call stack - iterative
#         queue = deque()
#         queue.append([root.left, root.right])

#         while queue:
#             pair = queue.popleft()
#             left,right = pair[0],pair[1]

#             if left is None and right is None:
#                 continue
#             if left is None or right is None:
#                 return False

#             if left.val==right.val:
#                 queue.appendleft([left.left,right.right]) # outward
#                 queue.appendleft([left.right,right.left]) # inward
#             else:
#                 return False
#         return True
        

        
        