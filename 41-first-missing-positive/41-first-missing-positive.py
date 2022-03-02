class Solution:
    def firstMissingPositive(self, a: List[int]) -> int:
        # cyclic sort
        i,n = 0,len(a)
        
        while i<len(a):
            correct_index = abs(a[i])-1
            
            # ignore negative and oob nums
            if a[i]>0 and a[i]<=n and a[i]!=a[correct_index]: 
                self.swap(a,i,correct_index)
            else:
                i += 1
        
        for i in range(n):
            if a[i]!= i+1:
                return i+1
        
        # if all values are sorted and nothing is oob in array
        # example a[1,2,3,4] then smallest missing is n+1 which is 5 here
        return n + 1 
            
    
    def swap(self,a,i,j):
        a[i],a[j] = a[j],a[i]
        
        