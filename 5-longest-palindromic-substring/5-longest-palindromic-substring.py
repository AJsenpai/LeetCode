class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return 
        
        result = ''
        
        for i in range(len(s)):
            # even
            temp = self.is_palindrome(s,i,i)
            if len(temp) > len(result):
                result = temp
            
            temp = self.is_palindrome(s,i,i+1)
            if len(temp)>len(result):
                result = temp
        return result
            
#             current_longest = max(current_longest, odd, even, key=lambda x : x[1]-x[0])     
#             longest = max(longest, current_longest, key=lambda x: x[1]-x[0])
            
#         return s[longest[0]: longest[1]]

    
    def is_palindrome(self,s,start,end):
        while start>=0 and end<=len(s)-1:
            if s[start]!=s[end]:
                break
            start -=1
            end +=1
        
        return s[start+1:end]
        
        
        
        
        
            