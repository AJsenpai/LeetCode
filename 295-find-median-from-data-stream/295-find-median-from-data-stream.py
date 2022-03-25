class MedianFinder:

    def __init__(self):
        self.small = [] # maxheap
        self.large = [] # minheap
        
    
    # insert priority for small - maxheap is more
    def addNum(self, num: int) -> None:
        heappush(self.small, -num)
        
        # every value in small_heap is <= values in large_heap
        if self.small and self.large and  -self.small[0] > self.large[0]:
            heappush(self.large, -heappop(self.small))
        
        # balance if height difference is greater than 1
        if len(self.small) > len(self.large) + 1:
            heappush(self.large, -heappop(self.small))
        
        if len(self.large) > len(self.small)+1:
            heappush(self.small, -heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small)>len(self.large):
            return -self.small[0]
        
        if len(self.large) > len(self.small):
            return self.large[0]
            
        return (-self.small[0]+self.large[0])/2
        
        
        
        
    
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()