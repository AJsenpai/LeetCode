class Solution:
    def myAtoi(self, string: str) -> int:
        # sanity check after string to array conversion
        # to handle "   " edge case
        s = list(string.strip())
        
        if not s:
            return 0                
        
        sign = -1 if s[0]=='-' else 1                
        
        if s[0] in ('+','-'):
            del s[0]
        
        i=0
        num = 0
        while i<len(s) and s[i].isdigit():
            num = num*10 + int(s[i])            
            i+=1
        
        
        # integer range = (2^31, -2^31)
        # if result is out of range return range
        num = max(-2**31, min(num * sign, 2**31-1))
        return num
        