class Solution:
    def nextGreaterElements(self, a: List[int]) -> List[int]:       
        stack = []
        result = []
        
        # to circle around keep stack pre-filled
        for i in reversed(a):
            stack.append(i)
        
        for i in reversed(range(len(a))):
            if not stack:
                result.append(-1)
            elif stack and stack[-1]>a[i]:
                result.append(stack[-1])
            elif stack and stack[-1]<= a[i]:
                while stack and stack[-1] <=a[i]:
                    stack.pop()
                if not stack:
                    result.append(-1)
                else:
                    result.append(stack[-1])
            
            stack.append(a[i])
        result.reverse()
        return result
                    
