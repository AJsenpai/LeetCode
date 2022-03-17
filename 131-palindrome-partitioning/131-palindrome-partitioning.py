class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output=  []
        result = []
        self.solve(s,0,len(s),output,result)
        return result
    
    def solve(self, s,start,end,output,result):
            
            if start==end:
                result.append(output[:])
                return 
            
            for i in range(start,end):
                curr_word = s[start:i+1]
                
                if curr_word == curr_word[::-1]:
                    output.append(curr_word)
                    self.solve(s,i+1,end,output,result)
                    output.pop()
            
        