class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
    
        buffer = ['']*len(digits)
        result = []
        self.solve(digits,buffer,0,0,result)
        return result
    
    def solve(self,phone,buffer,bufferIdx,startIdx,result):
        if bufferIdx == len(buffer):
            result.append(''.join(buffer))
            return 
        
        if startIdx==len(phone):
            return 
        
        letters = self.getLetters(phone[startIdx])
        
        for letter in letters:
            buffer[bufferIdx] = letter
            self.solve(phone,buffer,bufferIdx+1,startIdx+1,result)
    
    def getLetters(self, nums):
            letters = {
                '1': '',
                '2': 'abc',
                '3': 'def',
                '4': 'ghi',
                '5': 'jkl',
                '6': 'mno',
                '7': 'pqrs',
                '8': 'tuv',
                '9': 'wxyz',
                '0': ''
                
            }
            
            return letters[nums]
        