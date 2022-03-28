# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> List[List[int]]:
        all_path = []
        curr_path = []
        self.solve(root,target, curr_path,all_path)
        return all_path
    
    def solve(self,curr_node,target, curr_path,all_path):
        # base case - leaf node
        if curr_node is None:
            return 
        
        curr_path.append(curr_node.val)
        
        if (curr_node.val == target and 
            curr_node.left is None and 
            curr_node.right is None
           ):
            all_path.append(list(curr_path)) # copy 
        
        else:
            self.solve(curr_node.left, target - curr_node.val, curr_path, all_path)
            self.solve(curr_node.right, target - curr_node.val, curr_path, all_path)
        
        del curr_path[-1]
            
            
        