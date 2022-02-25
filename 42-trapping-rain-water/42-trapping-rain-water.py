class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        Two ways to solve this problem 
        1. using stack : O(N) T | O(N)  S     (readable)
        2. Using 2 Pointers : O(N) T | O(1) S (confusing)
        '''
        
        ## using stack : 
        # TO DO:
        
        ## using 2 pointers
        
        # two longest boundaries at any point
        leftMax,rightMax = height[0], height[-1]
        
        # calculate the water trap bw longest boundaries        
        left,right = 0,len(height)-1
        
        result = 0
        while left<=right:
            
            # left bounary is smaller than right boundary
            if leftMax < rightMax:
                
                if height[left]>leftMax:
                    leftMax = height[left]
                else:
                    result += leftMax - height[left]
                    
                left += 1
            
            else:
                 
                    if height[right]>rightMax:
                        rightMax = height[right]
                    else:
                        result += rightMax - height[right]
                    
                    right -= 1        
                    
        return result                
                