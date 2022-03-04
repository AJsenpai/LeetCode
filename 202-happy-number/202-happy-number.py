class Solution:
    def isHappy(self, n: int) -> bool:
        
        slow = fast = n
        while True:
            slow = self.square(slow)
            fast = self.square(self.square(fast))
            if slow == fast:
                break
        return slow==1
    
    def square(self, num):
        add = 0
        while num:
            digit = (num%10)
            add += digit * digit
            num = num //10
        return add
            
        