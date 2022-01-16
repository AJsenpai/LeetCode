class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start,end = 0,0
        char_count = {}
        max_count = 0
        max_length= 0 
        while end<len(s):
            right_char = s[end]
            if right_char not in char_count:
                char_count[right_char] = 0 
            char_count[right_char] += 1
            
            max_count = max(max_count, char_count[right_char])
            
            if end-start+1 <= max_count+k:
                max_length = max(max_length, end-start + 1)
            
            while end-start+1 > max_count + k:
                left_char = s[start]
                char_count[left_char]  -= 1
                if char_count[left_char]==0:
                    del char_count[left_char]
                start += 1                        
            end+= 1
        return max_length
            
        