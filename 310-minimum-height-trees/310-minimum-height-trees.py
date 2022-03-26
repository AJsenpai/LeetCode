class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n<=0:
            return 
        
        if n==1: # single node as 0 inDegree
            return [0] 
        # inDegree, graph, sources
        inDegree = {i:0 for i in range(n)}
        graph = {i:[] for i in range(n)}
        
        # unidirected
        for edge in edges:
            u,v = edge[0],edge[1]
            graph[u].append(v)
            graph[v].append(u)
            
            inDegree[u] += 1
            inDegree[v] += 1
        
        sources =deque()
        for key in inDegree:
            if inDegree[key]==1:
                sources.append(key)
        
        total_nodes = n
        while total_nodes>2:
            leaves_size = len(sources)
            total_nodes -= leaves_size
            
            for _ in range(leaves_size):
                node = sources.popleft()
                for child in graph[node]:
                    inDegree[child] -= 1
                    if inDegree[child]==1: # change
                        sources.append(child)
        return list(sources)
            
            
            
            
            
            
            
        