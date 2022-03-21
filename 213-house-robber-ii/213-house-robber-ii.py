class Solution:
    def rob(self, nums: List[int]) -> int:                
        n = len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        
        plan_a = self.rob_helper(nums,1,n)
        plan_b = self.rob_helper(nums,0,n-1)
        return max(plan_a,plan_b)
        
    
    def rob_helper(self, a,start,end):
        fib1,fib2 = 0,0
        for i in range(start,end):
            total = max(fib1+a[i], fib2)
            fib1 = fib2
            fib2 = total
        return total
    
        