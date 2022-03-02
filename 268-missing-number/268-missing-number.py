class Solution:
    def missingNumber(self, a: List[int]) -> int:
            # cyclic Sort
            i,n =0, len(a)
            while i < n:
                correct_index = a[i] # contains 0
                if a[i]<n and a[i]!= a[correct_index]:
                    self.swap(a,i,correct_index)
                else:
                    i += 1
            
            for i in range(n):
                if a[i]!= i :
                    return i
            
            return n
    
    def swap(self,a,i,j):
        a[i],a[j] = a[j],a[i]
                
        
#         # using xor with range 
#         # if you xor number with itself it cancel out
#         result = 0
#         # xor with range
#         for n in range(len(nums)+1):
#             result = result ^ n
        
#         # xor with numbers
#         for i in nums:
#             result = result ^ i
        
#         return result
            
        
        