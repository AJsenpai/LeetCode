class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        op = []
        self.solve(nums,0,op,result)
        return result
        
    def solve(self, ip,i,output,result):
        if i==len(ip):
            result.append(output[:])
            return 
        
        # include
        output.append(ip[i])
        self.solve(ip,i+1,output,result)
        output.pop()
        
        # dont include
        while i+1 < len(ip) and ip[i]==ip[i+1]:
            i +=1
        
        self.solve(ip,i+1,output,result)