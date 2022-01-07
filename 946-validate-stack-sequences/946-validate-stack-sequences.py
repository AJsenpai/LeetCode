class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack,index = [],0
        for val in pushed:
            stack.append(val)
            while stack and stack[-1]==popped[index]:
                stack.pop()
                index += 1
        return len(stack)==0
        