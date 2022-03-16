class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        output = []
        candidates.sort(reverse=True)
        self.solve(candidates,0,len(candidates),output,result,target)
        return result
    
    def solve(self,a,start,end,output,result,target):
        if target==0:
            result.append(output[:])            
        elif target>0:
            for i in range(start,end):
                if i>start and a[i]==a[i-1]:
                    continue
                output.append(a[i])
                
                # here we are passing i+1 cuz can we used only ONCE
                self.solve(a,i+1,end,output,result,target-a[i])
                output.pop()
        