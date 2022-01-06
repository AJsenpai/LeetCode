class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        string = list(s)
        stack = [] # store ( indices
        
        for idx, char in enumerate(string):
            if char=='(':
                stack.append(idx)
            elif char==')':
                if stack:
                    stack.pop()
                else:
                    string[idx]=''
        
        # no matchin parenthesis convert this ( to ''
        while stack:
            string[stack.pop()] = ''
        return ''.join(string)
        