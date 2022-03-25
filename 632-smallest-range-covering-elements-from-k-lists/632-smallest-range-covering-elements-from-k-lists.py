from heapq import *
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        start = 0
        end = float('inf')
        current_max = float('-inf')
        
        minheap = []
        for arr in nums:
            heappush(minheap, (arr[0],0,arr))
            current_max = max(current_max, arr[0])

        

        while len(minheap) == len(nums):
            number,index,array = heappop(minheap)
            index +=1
            
            if end-start > current_max-number:
                start=  number
                end = current_max
                
            if index < len(array):
                heappush(minheap, (array[index], index, array))
                current_max = max(current_max, array[index])
        
        return [start, end]
            