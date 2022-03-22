class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return 
        
        result = ''
        
        for i in range(len(s)):

            even = self.is_palindrome(s,i,i)
            odd = self.is_palindrome(s,i,i+1)            
            result = max(result,even,odd,key = len)
        
        return result
            


    
    def is_palindrome(self,s,start,end):
        while start>=0 and end<=len(s)-1:
            if s[start]!=s[end]:
                break
            start -=1
            end +=1
        
        return s[start+1:end]
        
        
        
        
        
            