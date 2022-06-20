class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # 2 pointers 
        
        # child of water trapping
        # just asking for max boundaries on both ends
        
        
        left,right = 0,len(height)-1        
        result = 0
        
        while left<right: # < we don't need =
            area = (right-left) * min(height[left],height[right])
            
            # need max area- moving towards maxArea
            if area>result:
                result = area
            
            if height[left] < height[right]:
                left +=1
            else:
                right -= 1
        return result
            

    
    