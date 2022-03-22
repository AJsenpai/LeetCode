class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return 
        longest=  [0,1]
        for i in range(1,len(s)):
            odd = self.is_palindrome(s,i-1,i+1) # ab(c)ba
            even = self.is_palindrome(s,i-1,i) # ab | cb
            
            curr_longest=  max(odd, even, key = lambda x: x[1]-x[0])
            longest = max(longest, curr_longest, key = lambda x: x[1]-x[0])
    
        return s[longest[0]:longest[1]]
    
    
    def is_palindrome(self,s,start,end):
        while start>=0 and end<len(s):
            if s[start]!=s[end]:
                break
            start -=1
            end +=1
        
        return [start+1,end]
        
        
        
        
        
            