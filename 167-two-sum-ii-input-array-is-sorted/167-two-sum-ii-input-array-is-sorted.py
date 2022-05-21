class Solution:
    def twoSum(self, a: List[int], target: int) -> List[int]:
        start,end = 0,len(a)-1
        
        while start<end:
            curr_sum = a[start]+a[end]
            
            if curr_sum==target:
                return [start+1,end+1]
            elif curr_sum<target:
                start +=1
            elif curr_sum>target:
                end -=1
        return -1
        
        