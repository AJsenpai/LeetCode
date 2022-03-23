class Solution:
    def flipAndInvertImage(self, a: List[List[int]]) -> List[List[int]]:
        
        for row in a:
            start,end = 0, len(row)-1
            while start<=end:
                if row[start] == row[end]:
                    row[start], row[end] = row[end]^1, row[start]^1
                start += 1
                end -=1
        return a
            
        
        
        
#         for sublist in image:
#             # flip horizontally - swap
#             sublist.reverse()
#             # invert - compliment
#             self.invert(sublist)            
#         return image
    
#     def invert(self,a):
#         for i,num in enumerate(a):
#             num ^= 1 #xor
#             a[i] = num
    
        