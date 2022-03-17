class Solution:
    def combine(self, n: int, size: int) -> List[List[int]]:
        result = []
        output = []
        self.solve(1,n+1,output,result,size)
        return result
    
    def solve(self,start,end,output,result,size):
        if size ==0:
            result.append(output[:])
        else:
            for i in range(start,end):
                output.append(i)
                self.solve(i+1,end,output,result,size-1)
                output.pop()