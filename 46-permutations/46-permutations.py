class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:    
        result = []
        self.solve(nums,0,len(nums),result)
        return result
    
    def solve(self,a,start,end,result):
        if start == end:            
            result.append(a[:])
            return
        
        for i in range(start,end):
            self.swap(a,start,i)
            self.solve(a,start+1,end,result) # v.imp
            self.swap(a,start,i) # backtrack
        
    def swap(self,a,i,j):
        a[i],a[j] = a[j],a[i]
        