class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        t = [0]*(n+1)
        t[n] = 1
        
        for i in reversed(range(n)):
            if s[i]!='0': # single digit
                t[i] += t[i+1]
            if i+1<n and (s[i]=='1' or s[i]=='2' and s[i+1]<='6'): # two digits
                t[i] += t[i+2]
        
        return t[0]
        
    
#     def solve(self,s,i):
#         if i==len(s):
#             return 1
        
#         result  = 0
        
#         if s[i]!='0':  # single digit
#             result += self.solve(s,i+1)
        
#         if i+1 < len(s) and (s[i]=='1' or s[i]=='2' and s[i+1]<='6'): # two digits
#             result += self.solve(s,i+2)
        
#         return result
        
        