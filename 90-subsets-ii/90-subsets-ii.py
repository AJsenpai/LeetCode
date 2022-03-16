class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        op = []
        self.solve(nums,0,len(nums),op,result)
        return result
        
    def solve(self,a,start,end,output,result):
        result.append(output[:])
        
        for i in range(start,end):
            
            # dont include
            if i>start and a[i-1]==a[i]:
                continue
            
            # include
            output.append(a[i])
            self.solve(a,i+1,end,output,result)
            output.pop() # backtrack
        

        

        
        
