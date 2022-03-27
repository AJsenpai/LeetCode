from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        mindepth = 0
        if not root:
            return mindepth
        queue = deque()
        queue.append(root)
        
        while queue:
            level_size = len(queue)
            mindepth += 1
            for _ in range(level_size):
                curr_node = queue.popleft()
                
                if curr_node.left is None and curr_node.right is None:
                    return mindepth
                
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
        return mindepth
        
        
        