class Solution:
    def isPalindrome(self, s: int) -> bool:
        
        # Solution 1
        # return str(s) == str(s)[::-1]
        
        # solution 2
        s = str(s)
        left,right = 0, len(s)-1
        while left<right:
            if s[left]!=s[right]:
                return False
            left +=1
            right -=1
        return True