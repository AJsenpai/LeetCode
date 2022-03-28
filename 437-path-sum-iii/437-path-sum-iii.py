# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:        
        current_path = []
        return self.solve(root, target, current_path)
    
    def solve(self,curr_node,target,current_path):
        # base case - leaf node
        if curr_node is None:
            return 0
        
        current_path.append(curr_node.val)
        
        path_count, curr_sum = 0,0
        for i in reversed(range(len(current_path))):
            curr_sum += current_path[i]
            if curr_sum==target:
                path_count+=1
        
        # hypothesis
        path_count += self.solve(curr_node.left, target, current_path)
        path_count += self.solve(curr_node.right, target, current_path)        
        
        
        
        # backtrack
        del current_path[-1]
        
        return path_count
    
    
        