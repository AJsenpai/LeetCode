class Solution:
    def reverseWords(self, s: str) -> str:
        
        def reverse_str(s,start,end):
            while start<end:
                s[start],s[end] = s[end],s[start]
                start+=1
                end -=1        

        s =  list(' '.join(s.split()))
        start=0        
        for end in range(len(s)):
            if s[end]==' ':
                reverse_str(s,start,end-1)
                start=end+1
        reverse_str(s,start,len(s)-1)
        return ''.join(s)
        
        
