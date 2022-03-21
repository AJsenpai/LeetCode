class Solution:
    def canJump(self, a: List[int]) -> bool:
        max_position,n = 0,len(a)
        
        for i,num in enumerate(a):
            if max_position < i:
                return False
            if max_position >= n-1:
                return True
            max_position = max(max_position, i + num)
        return False
    
#         if len(a)==1:
#             return True
        
#         max_position = 0
#         i = 0
        
        
#         while i<=max_position:
#             max_position = max(max_position, i + a[i])
#             if max_position >= len(a)-1:
#                 return True
#             i +=1
#         return False
        
        