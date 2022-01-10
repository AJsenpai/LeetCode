class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ## Logic
        ## 1. use stack to store the height and index 
        ## 2. if the heights are increasing order in other words
        ##    if the current height is greater than height on stack.top()
        ##    then append the current height and current_index 
        ## 3. if the height is smaller then stack.top then pop the top height
        ##    and compute its area , since the popped height is bigger then 
        ##    current height that current height can be exteneded backwards 
        ##    so we update the current_ids to popped index before pushing it to stack
        ## 4. if there are still elements left in stack that they may be a potential
        ##    candidate for max_area; so compute the max area for remaining element
        ## 5. return the max area
        
        ## O(n) T | O(n) S
        
        stack = [] # pair (index, height)
        max_area = 0
        for current_index, current_height in enumerate(heights):
            start = current_index
            while stack and stack[-1][1] > current_height:
                prev_index, prev_height = stack.pop()
                max_area = max(max_area, prev_height * (current_index - prev_index))
                start = prev_index
                
            stack.append((start, current_height))
            
        # remaining valus in stack could be potenetial max_area
        last_idx = len(heights)
        for curr_idx, height in stack:
            max_area = max(max_area, height*(last_idx - curr_idx))
        return max_area
                           

        
        
    
        