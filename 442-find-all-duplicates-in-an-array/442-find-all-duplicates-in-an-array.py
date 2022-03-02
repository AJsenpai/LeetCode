class Solution:
    def findDuplicates(self, a: List[int]) -> List[int]:
        # 287. follow up
        # here we cannot use a single loop like above
        # we need to use a seprate loop to find all missing 
        
        i, n = 0, len(a)
        
        while i<n:
            correct_index = a[i]-1
            
            if a[i] >0 and a[i]<=n and a[i]!=a[correct_index]:
                self.swap(a,i,correct_index)
            else:
                i += 1
        
        duplicates = []
        for i in range(n):
            if a[i]!=i+1:
                duplicates.append(a[i])
        
        return duplicates
    
    def swap(self,a,i,j):
        a[i],a[j] = a[j],a[i]
        
        
        