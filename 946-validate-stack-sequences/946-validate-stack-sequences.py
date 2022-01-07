class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
    # 1. Keep pushing pushed elements into stack if the top element
    #    on the stack is different from the current one of popped;
    # 2. Keep poping out of the top element from stack if it is same 
    #    as the current one of popped;
    # 3. Check if the stack is empty after loop.
    
        # O(N) T | O(N) S
        stack,index = [],0
        for val in pushed:
            stack.append(val)
            while stack and stack[-1]==popped[index]:
                stack.pop()
                index += 1
        return len(stack)==0
        