class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        result = self.getPow(abs(x),abs(n))
        
        if x<0 and n%2!=0:            
            result *= -1
            
        elif n<0:
            return 1/result
        
        return result
    
    def getPow(self,num,power):
        if power==0:
            return 1
        
        if power==1:
            return num
            
            
        halfPower = self.getPow(num, power//2)
        
        if power%2==0:
            return halfPower * halfPower
        else:
            return halfPower * halfPower * num
            
        
            
    
        