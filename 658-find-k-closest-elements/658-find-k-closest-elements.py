class Solution:
    def findClosestElements(self, a: List[int], k: int, target: int) -> List[int]:
        start,end = 0,len(a)-1
        
        while end-start >=k:
            # shrink window and move towards smaller value
            if abs(a[start] - target) > abs(a[end] - target):
                start += 1
            else:
                end -= 1
        
        return a[start:start+k]