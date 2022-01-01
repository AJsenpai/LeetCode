class Solution:
    def nextGreaterElements(self, a: List[int]) -> List[int]:       
        mapping,stack = {},[] # (idx, value) tuple

        for idx,x in enumerate(a):
            while stack and stack[-1][1]< x:
                index, val = stack.pop()
                mapping[index] = x
            stack.append((idx,x))

        # repeat the same thing again for circle
        for idx,x in enumerate(a):
            while stack and stack[-1][1]< x:
                index, _ = stack.pop()
                mapping[index] = x
            stack.append((idx,x))

        result = [-1]*len(a)

        for idx,x in enumerate(a):
            if idx in mapping:
                result[idx] = mapping[idx]
        return result