import re
class Solution:
    def strongPasswordCheckerII(self, s: str) -> bool:
        
        if len(s)<8:
            return False
        
        if (bool(re.search(r'[a-z]',s)) and 
            bool(re.search(r'[A-Z]',s)) and 
            bool(re.search(r'[0-9]',s)) and 
            bool(re.search(r'[^a-zA-Z0-9]',s))  and 
            not bool(re.search(r"(.)\1+", s))):
            return True
        return False
            