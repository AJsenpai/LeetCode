class Solution:
    
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count += self.isPalindrome(s,i,i) # odd
            count += self.isPalindrome(s,i,i+1) # even
            
        return count
            
    
    def isPalindrome(self,s,start,end):
        result = 0
        while start>=0 and end<=len(s)-1 and s[start]==s[end]:
            # if s[start]==s[end]:
                result +=1
                start -=1
                end += 1

        
        return result
                