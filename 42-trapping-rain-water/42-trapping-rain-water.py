class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        Using 2 pointers O(N) T | O(1) S        
        '''
        left,right = 0, len(height)-1
        leftMax,rightMax = height[0], height[-1]
        result = 0
        while left<=right:
            
            if leftMax < rightMax : # min height
                if height[left] > leftMax:
                    leftMax = height[left]
                else:
                    result += leftMax - height[left]
                left += 1
            
            else:
                if height[right] > rightMax:
                    rightMax = height[right]
                else:
                    result += rightMax - height[right]
                right -= 1
        
        return result
            
                
        
        '''
        using DP O(N) T | O(N) S
        
        max_left =  [4, 4, 4, 4, 4, 5]
        max_right = [5, 5, 5, 5, 5, 5]
        height =    [4, 2, 0, 3, 2, 5]
        
        minimumHeight = min(max_left,max_right) 
        
        if current_height < minHeight; 
            result += minHeight - currentHeight                
        '''
#         leftMax = [0]*len(height)
#         rightMax = [0]*len(height)
#         result = 0
#         for i in range(len(height)):
#             leftMax[i] = max(leftMax[i-1], height[i])
    
#         for i in reversed(range(len(height)-1)): # 4-->0
#             rightMax[i] = max(rightMax[i+1], height[i+1])
        
#         for i in range(len(height)):
#             minHeight = min(leftMax[i], rightMax[i])
#             if height[i] < minHeight:
#                 result += minHeight - height[i]
        
#         return result
                