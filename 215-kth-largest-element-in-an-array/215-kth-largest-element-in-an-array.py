from heapq import *
class Solution:
    def findKthLargest(self, a: List[int], k: int) -> int:
        n = len(a)
        minheap = []
        
        for i in range(n):
            heappush(minheap, a[i])
            
            if len(minheap) > k:
                heappop(minheap)
        
        return minheap[0]
                
        
        