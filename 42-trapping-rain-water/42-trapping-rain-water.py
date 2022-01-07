class Solution:
    def trap(self, height: List[int]) -> int:
        # max_left =  [4, 4, 4, 4, 4, 5]
        # max_right = [5, 5, 5, 5, 5, 5]
        # height =    [4, 2, 0, 3, 2, 5]
        
        # ans = min(max_left,max_right) 
        # if height < min; then min - height
        
        # ans =       [0, 2, 4, 1, 2, 0]
        
        leftMax = [0]*len(height)
        rightMax = [0]*len(height)
        result = 0
        for i in range(len(height)):
            leftMax[i] = max(leftMax[i-1], height[i])
    
        for i in reversed(range(len(height)-1)): # 4-->0
            rightMax[i] = max(rightMax[i+1], height[i+1])
        
        for i in range(len(height)):
            minHeight = min(leftMax[i], rightMax[i])
            if height[i] < minHeight:
                result += minHeight - height[i]
        return result
                