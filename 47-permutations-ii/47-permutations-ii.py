class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        output = []
        visited =[False]*len(nums)
        self.solve(nums,output,result,visited)
        return result
    
    def solve(self,a,output,result,visited):
        if len(output)== len(a):
            result.append(output[:])
            
        # else:
        for i in range(len(a)):
            # curr and prev are same and visited flag for prev is false
            
            if visited[i] or (i>0 and a[i-1]==a[i] and not visited[i-1]):
                continue
            
            visited[i] = True
            output.append(a[i])
            self.solve(a,output,result,visited)
            
            output.pop() # backtrack
            visited[i] = False
            
        