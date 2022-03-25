from heapq import *
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        minheap = [] # sortinf upto k
        for row in matrix:
            heappush(minheap, (row[0],0,row))
        
        number_count = 0
        while minheap:
            num,index,row = heappop(minheap)
            index +=1
            number_count +=1
            
            if number_count==k:
                break
            if index < len(row):
                heappush(minheap, (row[index],index,row))
        return num
            
            
        