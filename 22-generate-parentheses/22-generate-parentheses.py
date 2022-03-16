class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = ''
        result = []
        open_brackets = close_brackets = n
        self.solve(open_brackets,close_brackets,output,result)
        return result
    
    def solve(self,open_brackets,close_brackets,output,result):
        if open_brackets ==0 and close_brackets==0:
            result.append(output)
            return 
        
        # always have open brackets choice
        if open_brackets!=0:
            output1 = output[:]
            output1 += '('
            self.solve(open_brackets-1,close_brackets,output1,result)
        
        # close brackets choice only when close>open
        if close_brackets > open_brackets:
            output2 = output[:]
            output2+= ')'
            self.solve(open_brackets,close_brackets-1,output2,result)
            
        
        