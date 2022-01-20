class Solution:
    def splitArray(self, a: List[int], m: int) -> int:
        if m>len(a):
            return -1
        
        start = max(a)
        end = sum(a)
        result  = float('inf')
        while start<=end:
            mid = (start +end)//2 # max_sum
            if self.isValid(a,m,mid):
                result = mid
                end = mid - 1
            else:
                start = mid + 1
        
        # return sum(a) - result
        return result
    
    def isValid(self,arr,m,max_sum):
        split = 1
        add = 0 
        for num in arr:  
            add += num
            if add > max_sum:
                split+=1
                add = num
                
                if split>m:
                    return False       
        
        # return split <= m
        return True
        
            