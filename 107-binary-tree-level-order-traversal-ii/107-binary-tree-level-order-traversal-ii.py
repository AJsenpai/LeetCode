from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = deque()
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        
        while queue:
            level_size = len(queue)
            curr_level = []
            
            for _ in range(level_size):
                curr_node = queue.popleft()
                curr_level.append(curr_node.val)
                
                if curr_node.left:
                    queue.append(curr_node.left)
                
                if curr_node.right:
                    queue.append(curr_node.right)
                
            result.appendleft(curr_level)
        
        return list(result)
        