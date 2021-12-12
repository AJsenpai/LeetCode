class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        start=0
        end=len(s)-1
        while start<end:            
            if not s[start].isalpha(): 
                start+=1
            if not s[end].isalpha():
                end -=1
            if s[start].isalpha() and s[end].isalpha():
                self.swap(s,start,end)    
                start+=1
                end -=1
                
        return ''.join(s)
    
    def swap(self,a,i,j):
        a[i],a[j] = a[j],a[i]
        
        
        