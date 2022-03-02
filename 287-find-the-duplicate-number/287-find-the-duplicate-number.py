class Solution:
    def findDuplicate(self, a: List[int]) -> int:
        # cyclic sort
        i,n = 0,len(a)
        
        while i<n:
            correct_index = a[i]-1
            if a[i] != a[correct_index]:
                self.swap(a,i,correct_index)
            else:
                i+=1
        
        for i in range(n):
            if a[i]!=i+1:
                return a[i]
        
    
    def swap(self,a,i,j):
        a[i],a[j]=a[j],a[i]