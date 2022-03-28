from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        if not root:
            return result
        
        queue =deque()
        queue.append(root)
        
        while queue:
            level_size = len(queue)                        
            curr_sum = 0
            
            for i in range(level_size):
                curr_node = queue.popleft()
                curr_sum += curr_node.val
                
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            
            average = curr_sum/level_size
            result.append(average)
        
        return result
        
        
            
            
        