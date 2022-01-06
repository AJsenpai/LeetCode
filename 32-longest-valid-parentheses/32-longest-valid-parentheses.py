class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [[')', -1]]
        max_length = 0
        for idx,char in enumerate(s):
            if char==')' and stack[-1][0]=='(':
                stack.pop() # this is popped 
                
                # max_length is calculated after this 
                max_length = max(max_length, idx-stack[-1][1])
            else:
                stack.append([char,idx])
        return max_length
            
                    
        