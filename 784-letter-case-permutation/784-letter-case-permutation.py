class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        op = ''
        result= []
        self.solveLCP(s,op,result)
        return result
    
    def solveLCP(self, ip,output,result):
        if len(ip)==0:
            result.append(output)
            return
        
        if ip[0].isdigit():
            output1 = output[:]
            output1 += ip[0]
            ip = ip[1:]
            self.solveLCP(ip,output1,result)
        else:
            output1 = output[:]
            output2 = output[:]
            
            output1 += ip[0].lower()
            output2 += ip[0].upper()
            ip = ip[1:]
            self.solveLCP(ip,output1,result)
            self.solveLCP(ip,output2,result)
            
            
        