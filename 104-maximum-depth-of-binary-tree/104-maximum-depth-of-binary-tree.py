from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # height of BT - BFS, easy with DFS as well
        maxdepth = 0
        if not root:
            return maxdepth
        
        queue = deque()
        queue.append(root)
        while queue:
            level_size = len(queue)
            maxdepth += 1
            
            for _ in range(level_size):
                curr_node= queue.popleft()
                
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
        return maxdepth
            
        