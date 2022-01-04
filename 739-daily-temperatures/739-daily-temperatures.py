class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:       
        result = [0]*len(temp)
        stack = [] # old day indexes with decreasing temp, monotonic stack
        
        for curr_day, curr_temp in enumerate(temp):
            while stack and temp[stack[-1]] < curr_temp:
                previous_day = stack.pop()
                result[previous_day] = curr_day - previous_day
            stack.append(curr_day)
        return result
        
        