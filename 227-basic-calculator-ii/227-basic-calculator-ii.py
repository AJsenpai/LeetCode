class Solution:
    def calculate(self, exp: str) -> int:
            if not exp:
                return 0
            stack = []
            all_operators = {'+','-','*','/'}
            curr_num = 0 # this is what we push in stack    
            operator = '+'
            for i in range(len(exp)):
                char = exp[i]

                if char.isdigit():
                    curr_num = curr_num * 10 + int(exp[i])

                if char in all_operators or i==len(exp)-1:
                    self.process(operator, curr_num, stack)
                    curr_num = 0
                    operator =char # current_operator
            return sum(stack)
    
    def process(self, operator, num , stack):
            if operator == '+':
                stack.append(num)
            elif operator == '-':
                stack.append(-num)
            elif operator == '*':
                stack.append(stack.pop() * num)
            elif operator == '/':
                stack.append(int(stack.pop() / num)) # edge case // won't work        
        
