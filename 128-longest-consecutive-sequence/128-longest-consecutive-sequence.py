class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        
        longest = 0
        for n in nums:
            if (n - 1) not in nums_set: # new sequence
                length = 1                
                
                # check if incresing sequence is present in hashset
                while (n + length) in nums_set:
                    length += 1
                    
                longest = max(longest,length)
        return longest
                

        
        
        
        
        
        
        
#         # using sort        
#         a.sort()
        
#         longest,curr_longest = 0, min(1,len(a))
        
#         for i in range(1,len(a)):
#             if a[i]==a[i-1]: # consecutive + duplicates
#                 continue
#             if a[i] == a[i-1]+1: # consecutive + increasing 
#                 curr_longest += 1
#             else:  # not consecutive, new num chain is starting like 100,200
#                 longest = max(longest,curr_longest) 
#                 current_longest = 1
        
#         return max(longest,curr_longest)
        
        

            
        