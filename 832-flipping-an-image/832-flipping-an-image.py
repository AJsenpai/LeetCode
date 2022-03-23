class Solution:
    def flipAndInvertImage(self, a: List[List[int]]) -> List[List[int]]:
        
        """
        Bitwise XOR --> 0^1 = 1, 1^1 =0 (invert)

        After reviewing some examples you will notice the following patterns:
        1.  Look at first and last value of row. If they are the same (1,1 or 0,0), 
            they will be flipped in the output. If they are different (1,0 or 0,1), 
            they do not change. Work your way inward to the middle of the list 
            applying this rule.

        2.  If the row has an odd number of entries, the middle value always flips. 
            For example if len(row) = 5, then row[2] must change values.

        """

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
    
        