class Solution:
    def largestRectangleArea(self, a: List[int]) -> int:   
#         # Brute Force
#         # O(n^2) T | O(1) S
#         # The approach is to find the right smaller and left smaller element and
#         # find the largest Rectangle area in Histogram.

#             max_area = 0
#             for i in range(len(a)):
#                 min_height = float("inf")
#                 for j in range(i, len(a)):
#                     min_height = min(min_height, a[j])
#             return max_area

            right = self.nearestSmallerRight(a)
            left = self.nearestSmallerLeft(a)

            width = [None] * len(a)
            for i in range(len(a)):
                width[i] = right[i] - left[i] - 1

            max_area = float("-inf")
            for i in range(len(a)):
                current_area = a[i] * width[i]
                max_area = max(max_area, current_area)

            return max_area

        # helper code
    def nearestSmallerRight(self, a):
        pseudoIndex = len(a)
        stack = []  # paid [NSR, NSRindex]
        result = []
        for i in reversed(range(len(a))):
            if not stack:
                result.append(pseudoIndex)

            elif stack and stack[-1][0] < a[i]:
                result.append(stack[-1][1])

            elif stack and stack[-1][0] >= a[i]:
                while stack and stack[-1][0] >= a[i]:
                    stack.pop()
                if not stack:
                    result.append(pseudoIndex)
                else:
                    result.append(stack[-1][1])

            stack.append([a[i], i])

        result.reverse()
        return result


    def nearestSmallerLeft(self, a):
        pseudoIndex = -1
        stack = []
        result = []
        for i in range(len(a)):
            if not stack:
                result.append(pseudoIndex)

            elif stack and stack[-1][0] < a[i]:
                result.append(stack[-1][1])

            elif stack and stack[-1][0] >= a[i]:
                while stack and stack[-1][0] >= a[i]:
                    stack.pop()
                if not stack:
                    result.append(-1)
                else:
                    result.append(stack[-1][1])

            stack.append([a[i], i])

        return result

                           

        
        
    
        