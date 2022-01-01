class Solution:
    def isValid(self, s: str) -> bool:
        opening_brackets = '[({<'
        closing_brackets = '])}>'
        mapping = {'}':'{', ')':'(', ']':'[', '>':'<'}
        stack = []
        for i in s:
            if i in opening_brackets:
                stack.append(i)
            elif i in closing_brackets:
                if not stack:
                    return False
                elif stack[-1] == mapping[i]:
                    stack.pop()
                else:
                    return False
        
        return len(stack)==0
                
        