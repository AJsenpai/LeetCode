class Solution:
    def canJump(self, a: List[int]) -> bool:
        n = len(a)
        max_position = 0
        i = 0                
        while i<=max_position:
            max_position = max(max_position, i + a[i])
            if max_position >= n-1:
                return True
            i +=1
        return False

    

#         max_position,n = 0,len(a)
        
#         for i,num in enumerate(a):
#             if max_position < i:
#                 return False
#             if max_position >= n-1:
#                 return True
#             max_position = max(max_position, i + num)
#         return False
    


        

        
        