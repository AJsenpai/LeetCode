class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # variable size window
        start,end = 0,0
        hashmap = {}
        max_count  = 0
        max_length = 0
        
        while end < len(s):

            right_char = s[end]
            if right_char not in hashmap:
                hashmap[right_char] = 0
            hashmap[right_char] += 1
            
            # max_repeating char so far 
            max_count = max(max_count, hashmap[right_char])
            
            if end-start+1 <= k + max_count: # ** <=
                max_length = max(max_length, end-start+1)
            
            while end-start+1 > k + max_count:
                left_char = s[start]
                hashmap[left_char] -= 1
                
                if hashmap[left_char]==0:
                    del hashmap[left_char]
                start += 1
            end +=1
        
        return max_length
                
                
