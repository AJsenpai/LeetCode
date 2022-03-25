from heapq import *
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap =  {}
        for t in tasks:
            if t not in hashmap:
                hashmap[t] = 0
            hashmap[t] += 1
        
        
        maxheap = []        
        for task,count in hashmap.items():
            heappush(maxheap, (-count, task))
        
        interval_count = 0 
        while maxheap:
            waiting_list = []
            total_task = n+1
            
            while total_task>0 and maxheap:
                interval_count +=1
                count,task = heappop(maxheap)
                
                if -count>1:
                    waiting_list.append((count+1,task))
                
                total_task -= 1
            
            for count,char in waiting_list:
                heappush(maxheap, (count,task))
            
            if maxheap:
                # if total_task is not 0 after processing heap then that is its idle time
                interval_count += total_task
        return interval_count
            