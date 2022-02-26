class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        index1 = len(s)-1
        index2 = len(t)-1
        
        while index1>=0 or index2>=0:
            
            p1 = self.getNextValidIndex(s, index1)
            p2 = self.getNextValidIndex(t, index2)
            
            if p1<0 and p2<0:
                return True
            
            if p1<0 or p2<0:
                return False
            
            if s[p1] != t[p2]:
                return False
            
            index1 = p1 -1
            index2 = p2 - 1
        
        return True
    
    def getNextValidIndex(self, s,idx):
        backspace = 0
        
        while idx>=0:
            
            if s[idx]=='#':
                backspace += 1
            
            elif backspace > 0:
                backspace -= 1
            
            else:
                break
            
            idx -= 1
        
        return idx
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        