class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        if not s:
            return 
        if len(s)==1 and s!=c:
            return 
        if len(s)==1 and s==c:
            return 0
            
        result = []
        
        left_char_idx = float('-inf')
        
        for i,char in enumerate(s):
            if char==c:
                left_char_idx = i
            result.append(i-left_char_idx)
        
        right_char_idx = float('inf')
        for i in reversed(range(len(s))):
            char = s[i]
            if char==c:
                right_char_idx = i
            result[i] = min(result[i], right_char_idx - i)
        
        return result
            
            
            
        