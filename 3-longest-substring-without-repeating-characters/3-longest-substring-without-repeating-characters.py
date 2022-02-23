class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # variable size sliding window
        start,end = 0,0
        hashmap = {}
        max_length = 0
        
        while end < len(s):
            right_char = s[end]
            if right_char not in hashmap:
                hashmap[right_char] = 0
            hashmap[right_char] +=1
            
            # hashmap has unique char at each time
            if end-start+1 == len(hashmap):
                max_length = max(max_length, end-start+1)
            
            # repeating char in hashmap
            if len(hashmap) < end-start+1:
                
                while len(hashmap) < end-start+1:
                    left_char = s[start]
                    hashmap[left_char] -= 1

                    if hashmap[left_char]==0:
                        del hashmap[left_char]
                
                    start+=1
            end +=1
        
        return max_length