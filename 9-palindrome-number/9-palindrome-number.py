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
    
        # solution3 
        # new_num = 0 
        # x = s
        # while x>0:
        #     new_num = (new_num*10)+ (x%10)
        #     x = x//10
        # return new_num == s
    
   
