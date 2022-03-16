class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        op = []
        self.solve(nums,op,result)
        return result
    
    def solve(self, ip, output,result):
        if len(ip)==0:
            result.append(output)
            return
        
        output1 = output[:]
        output2 = output[:]
        
        output2.append(ip[0])
        
        ip = ip[1:]
        
        self.solve(ip,output1,result)
        self.solve(ip,output2,result)
        