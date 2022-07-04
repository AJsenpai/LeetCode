class Solution:
    def countAndSay(self, n: int) -> str:
        
        # Solution 2
        sequence = [1]
        for _ in range(n-1):
            next_seq = []
            for num in sequence:
                if not next_seq or next_seq[-1]!=num:
                    next_seq += [1, num]
                else:
                    next_seq[-2] +=1
            sequence = next_seq
        
        return ''.join(map(str, sequence))
            

        
        
        # Solution 1
        
#         # returns the next sequence
#         # example s=21 --> 1211
#         def next_number(s):
            
#             result = []
#             i=0
        
#             while i <len(s):
#                 count = 1
#                 while i+1 < len(s) and s[i]==s[i+1]:
#                     count+=1
#                     i+=1
#                 result.append(str(count)+s[i])
#                 i+=1
            
#             return ''.join(result)
        
#         s = "1"
#         for _ in range(n-1):
#             s = next_number(s)
#         return s
            