from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        
        queue = deque()
        queue.append(root)
            
        left_to_right = True
        while queue:
            level_size = len(queue)
            curr_level = deque()
            
            for _ in range(level_size):
                curr_node = queue.popleft()
                
                if left_to_right:
                    curr_level.append(curr_node.val)
                else:
                    curr_level.appendleft(curr_node.val)
                    
                
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
                
            result.append(list(curr_level))
            left_to_right = not left_to_right
        
        return result