class Solution:
    def threeSumClosest(self, a: List[int], target: int) -> int:
        if len(a) <3:
            return
        
        a.sort()
        result = a[0]+a[1]+a[2]
        for i in range(len(a)-2):
            left = i+1
            right = len(a)-1
            
            while left < right:
                curr_sum = a[i]+a[left]+a[right]               
                
                if curr_sum==target:
                    return curr_sum
                
                if abs(curr_sum - target)<abs(result-target):
                    result = curr_sum
                
                elif curr_sum<target:
                    left +=1
                elif curr_sum > target:
                    right -=1
                    
        return result 
    
    def findClosest(self, result,curr_sum,target):
        if result==0:
            return curr_sum
        
        if abs(target-result) < abs(target - curr_sum):
            return result
        else:
            return curr_sum
        
        