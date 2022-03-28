import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = collections.defaultdict(list)
        
        # build graph
        def dfs(node, parent_node):
            if parent_node:
                graph[node].append(parent_node)
            
            if node.left:
                graph[node].append(node.left)
                dfs(node.left, node)
            
            if node.right:
                graph[node].append(node.right)
                dfs(node.right, node)
        
        dfs(root, None)
        
        # BFS
        result = []
        visited = {target}
        def bfs(node,k):
            if k==0:
                result.append(node.val)
            else:
                visited.add(node)
                for child in graph[node]:
                    if child not in visited:
                        bfs(child, k-1)
        bfs(target, k)
        
        return result
            
            
        
        
        
        