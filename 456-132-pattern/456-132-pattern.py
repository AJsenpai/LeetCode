class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        ## Logic ##
        ## Brute force - use 3 loops for i,j,k and compare -> O(N^3) T
        
        ## Optimal Solution
        ## condition - i<k<j
        
        ## 1. create a minimum array (min_so_far) this will be our i
        ## 2. start iterating reverse in array (this is for j)
        ## 3. we will use stack and stack.top to determine k (2 in 132 pattern)
        ## 4. At any position we push element if it is greater then minimum 
        ##    element (possible 2 in 132 patter since 2>1)
        ## 5. At any position, we check if stack.top is less than or equal to min
        ##    element; if so we pop the elements using loop (invalid element for 132)
        ## 6. satisfying condition: at any stage if 
        ##    min_so_far[i] < stack[-1] < nums [i] 
        ##        i             k            j
        ## Edge Case: before checking 4,6 pop the invalid elements first before 
        ##            inserting new current element
        ## O(N) T | O(N) S
            
        if len(set(nums))<3:
            return False
        
        # 1
        min_nums = [nums[0]]
        for i in range(1, len(nums)):
            min_nums.append(min(min_nums[-1], nums[i]))
        
        stack = []
        # i= len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            # 4
            if nums[i] > min_nums[i]:
                # 5
                while stack and stack[-1] <= min_nums[i]:
                    stack.pop()
                
                #6
                if stack and min_nums[i] < stack[-1] < nums[i]:
                    return True
                
                #4
                stack.append(nums[i])
        
        return False
                
            
        
        
                
        
        
        
        
        
        
   

