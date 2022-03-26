from collections import deque
class Solution:
    def findOrder(self, vertices: int, edges: List[List[int]]) -> List[int]:
        if vertices<=0:
            return []
        sortedOrder = []
        
        # inDegree, graph, sources
        inDegree = {i:0 for i in range(vertices)}
        graph = {i:[] for i in range(vertices)}
        
        for edge in edges:
            parent,child = edge[0],edge[1]
            graph[parent].append(child)
            inDegree[child]+=1
        
        sources = deque()
        for key in inDegree:
            if inDegree[key]==0:
                sources.append(key)
        
        # topological sort + BFS
        while sources:
            node = sources.popleft()
            sortedOrder.append(node)
            for child in graph[node]:
                inDegree[child]-=1
                if inDegree[child]==0:
                    sources.append(child)
        
        if len(sortedOrder)!= len(inDegree):
            return []
        
        sortedOrder.reverse()
        return sortedOrder
        
        