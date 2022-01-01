class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
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
            
        
            
            
            
        