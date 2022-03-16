class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        output = ''
        result = []        
        self.solve(s,output,result)
        return result
    
    def solve(self, ip,output,result):
        if len(ip)==0:
            result.append(output)
            return
        
        # getting 2 choices only when input is alphabet
        if ip[0].isalpha():
            output1 = output[:]
            output2 = output[:]
            
            output1 += ip[0].lower()
            output2 += ip[0].upper()
            
            ip = ip[1:]            
            self.solve(ip,output1,result)
            self.solve(ip,output2,result)
        
        else: #digit
            output1 = output[:]
            output1 += ip[0]
            
            ip = ip[1:]
            self.solve(ip,output1,result)
    
    
    
        
        