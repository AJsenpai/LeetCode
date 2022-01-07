class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        1. build hashmap to store number: its next bigger
        2. loop: 
            use stack; so long the stack has value and stack.top < current number
            hashmap[stack.pop()] = current_number
           stack.push(current_numer)
         
         3. at last stack will only has number which doesnt have any next_bigger
         4. iterate over nums1 and check if the value is present in hash
            if yes; then pop its next bigger else add -1 
            
            O(n) T | O(n) S
        '''
        mapping,stack = {},[]        
        # build hashmap with key= number, val = nextbigger 
        for x in nums2:
            while stack and stack[-1]< x:
                # for all these numbers x is the next bigger
                mapping[stack.pop()] = x
            stack.append(x)
        
        result = []
        
        for x in nums1:
            if x in mapping:
                result.append(mapping[x])
            else:
                result.append(-1)
        return result
            
        
            
            
            
        