class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort(reverse=True)
        output = []
        self.solve(candidates,0,len(candidates),output,result,target)
        return result
    
    def solve(self,a,start,end,output,result,target):
        if target==0:
            result.append(output[:])
            return
        
        elif target>0:
            for  i in range(start,end):
                output.append(a[i])
                
                # here we are passing i cuz can we used unlimited times
                self.solve(a,i,end,output,result,target-a[i]) 
                output.pop()
        