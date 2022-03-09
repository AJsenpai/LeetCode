class Solution:
    def strStr(self, string: str, pattern: str) -> int:
        # using kmp algorithm O(m+n)T
        
        if not pattern:
            return 0
        
        lps_table = self.build_pattern(pattern)
        
        m = len(string)
        n = len(pattern)
        i,j= 0,0
        
        while i<m:
            if string[i] == pattern[j]:
                i += 1
                j +=1
                if j== n:
                    return i - n
            else:
                if j!=0:
                    j = lps_table[j-1]
                else:
                    i +=1
        return -1
                
    
    
    def build_pattern(self,pattern):
        lps = [0]*len(pattern)
        i = 1
        j = 0
        
        while i < len(pattern):
            if pattern[i]==pattern[j]:
                j += 1 # adding values in lps from 1 onwards
                lps[i]= j 
                i += 1
            else:
                if j!=0:
                    j = lps[j-1]
                else:
                    i += 1
        return lps
                    
        
        
        
        