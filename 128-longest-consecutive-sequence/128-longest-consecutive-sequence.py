class Solution:
    def longestConsecutive(self, a: List[int]) -> int:
        hashset = set(a)
        
        longest = 0
        for nums in a:
            if nums-1 not in hashset:
                count = 1
                
                n = nums +1
                while n in hashset:
                    count += 1
                    n += 1
                longest = max(longest,count)
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
        
        

            
        