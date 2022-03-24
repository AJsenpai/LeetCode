from heapq import *
class Solution:
    def findKthLargest(self, a: List[int], k: int) -> int:
        k = k-1
        return self.quickSelect(a,k,0,len(a)-1)
    
    def quickSelect(self, a,k,start,end):
        p = self.partition(a,start,end)
        
        if p==k:
            return a[p]
        elif p>k:
            return self.quickSelect(a,k,start,p-1)
        
        elif p<k:
            return self.quickSelect(a,k,p+1,end)
    
    def partition(self, a,low,high):
        if low==high:
            return low
        
        pivot = a[high]
        
        for i in range(low,high): # high is excluded 
            if a[i]>=pivot:
                self.swap(a,i,low)
                low+=1
        
        self.swap(a,low,high) # right place of pivot
        return low
    
    def swap(self,a,i,j):
        a[i],a[j] = a[j],a[i]
                
        
        

        
        
        
        
# using heap:        
#         n = len(a)
#         minheap = []
        
#         for i in range(n):
#             heappush(minheap, a[i])
            
#             if len(minheap) > k:
#                 heappop(minheap)
        
#         return minheap[0]
                
        
        