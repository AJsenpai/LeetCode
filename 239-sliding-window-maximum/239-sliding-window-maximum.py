from collections import deque

class Solution:
    def maxSlidingWindow(self, a: List[int], k: int) -> List[int]:
        # fixed size window: asking for max in each window : QUEUE
        result = []
        start,end = 0,0
        queue = deque()
        
        while end<len(a):
            
            while queue and queue[-1] < a[end]:
                queue.pop()
            queue.append(a[end])
            
            if end-start+1==k:
                result.append(queue[0])
                
                if a[start] == queue[0]:
                    queue.popleft()
                start+=1
            end+=1
        return result
        