class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # O(N) T | O(N) S
        # using prefix and postfix product arrays 
        # to calcualte the product except itself array
        
#         n = len(nums)
#         prefix = [1]*n
#         postfix = [1]*n
#         product = [1]*n
        
#         for i in range(1,n):
#             prefix[i] = prefix[i-1]*nums[i-1]
        
#         for i in reversed(range(0,n-1)):
#             postfix[i] = postfix[i+1]* nums[i+1]
        
#         for i in range(n):
#             product[i] = prefix[i]*postfix[i]
        
#         return product
    
        # O(N) T | O(1) S
        # using prefix and postfix pointers instead of arrays
        
        n = len(nums)
        product = [1]*n
        
        prefix = 1                
        for i in range(n):
            # first add then calculate next prefix product
            product[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in reversed(range(n)):
            product[i] *= postfix
            postfix *= nums[i]
        
        return product
            
            
        
        
        
        
        