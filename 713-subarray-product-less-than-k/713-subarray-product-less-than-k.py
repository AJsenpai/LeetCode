from collections import deque
class Solution:
    def numSubarrayProductLessThanK(self, a: List[int], target: int) -> int:
        # 2 pointers + Sliding window
        # O(N^3) T | O(N^2) S
        
        product = 1
        count = 0
        
        start,end = 0,0
        
        while end < len(a):
            product *= a[end]
            
            while product >=target and start<end:
                product = product//a[start]
                start += 1
            
            # getting result subarrays
            # n + (n_1) + (n-2) .. + 1
            # temp_list =deque()
            # for i in range(end,start+1,-1):
            #     temp_list.appendleft(a[i])
            #     result.append([temp_list])

            # just need the count
            if product < target:
                count += end-start+1                     
            
            end +=1
        
        return count
            
        
