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
    
#     def solve(self, a, start,end,output,result):
#         result.append(output[:])

#         for i in range(start,end):
#             output.append(a[i])
#             self.solve(a,i+1,end,output,result)
#             output.pop()
        
        