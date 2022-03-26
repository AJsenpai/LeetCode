from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # BFS
        n = len(graph)
        colors = [None]*n # initially all nodes are not colored
        
        for i in range(n):
            if colors[i] is not None:
                continue
            
            colors[i] = True
            queue = deque([i])
            
            while queue:
                node = queue.popleft()
                
                for child in graph[node]:
                    if colors[child] is None:
                        colors[child] = not colors[node] # set an opposite color of P node
                        queue.append(child)
                    elif colors[child] == colors[node]: # inconsistecny
                        return False
        return True
        
        