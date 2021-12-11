class Solution:
    def validPalindrome(self, s: str) -> bool:
        left,right = 0,len(s)-1
        while left<right:
            if s[left]!=s[right]:
                exclude_left = s[left+1:right+1] # rightis included
                exclude_right = s[left:right]
                return self.isPalindrome(exclude_left) or self.isPalindrome(exclude_right)
            left += 1
            right -=1
        return True
    
    def isPalindrome(self,string):
        return string==string[::-1]
                    
                