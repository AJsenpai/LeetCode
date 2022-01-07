class Solution:
    def trap(self, height: List[int]) -> int:
        # max_left =  [4, 4, 4, 4, 4, 5]
        # max_right = [5, 5, 5, 5, 5, 5]
        # height =    [4, 2, 0, 3, 2, 5]
        
        # ans = min(max_left,max_right) 
        # if height < min; then min - height
        
        # ans =       [0, 2, 4, 1, 2, 0]
        maxes = [0]* len(height)
        leftMax = 0
        for i in range(len(height)):
            current_height = height[i]
            maxes[i] = leftMax # savind for right max compare
            leftMax = max(leftMax, current_height)
            
        rightMax = 0
        for i in reversed(range(len(height))):
            current_height = height[i]
            min_height = min(rightMax, maxes[i])
            
            if current_height < min_height:
                maxes[i] = min_height - current_height                                 
            else:
                maxes[i] = 0
            rightMax = max(rightMax, current_height)
        
        return sum(maxes)
        
        
        