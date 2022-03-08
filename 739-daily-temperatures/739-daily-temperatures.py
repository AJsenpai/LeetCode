class Solution:
    def dailyTemperatures(self, a: List[int]) -> List[int]:       
            ngr = self.ngr_dt(a)

            result = []
            for i in reversed(range(len(a))):
                if ngr[i] > 0:
                    result.append(ngr[i] - i)
                else:
                    result.append(0)

            result.reverse()
            return result


    def ngr_dt(self, a):
        stack = []  # NGR, NGR index
        result = []
        for i in reversed(range(len(a))):
            if not stack:
                result.append(-1)

            elif stack[-1][0] > a[i]:
                result.append(stack[-1][1])

            elif stack[-1][0] <= a[i]:
                while stack and stack[-1][0] <= a[i]:
                    stack.pop()

                if not stack:
                    result.append(-1)
                else:
                    result.append(stack[-1][1])

            stack.append([a[i], i])

        result.reverse()
        return result

        
        