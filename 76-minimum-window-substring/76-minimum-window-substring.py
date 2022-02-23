class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start,end = 0,0
        char_count = {}
        min_length = len(s)+1 # entire string could be min length
        match = 0
        for char in t:
            if char not in char_count:
                char_count[char] = 0
            char_count[char] += 1
        
        while end<len(s):
            right_char = s[end]
            if right_char in char_count:
                char_count[right_char] -= 1
                if char_count[right_char] == 0:
                    match += 1
            
            while match == len(char_count):
                if min_length>end-start+1:
                    min_length = end-start+1
                    substring_start = start
                
                left_char = s[start]
                # -ve shows we have extra in char_count                
                if left_char in char_count:
                    if char_count[left_char]==0:
                        match -= 1 # decrement char count before putting char back
                    char_count[left_char] += 1 # put char back
                start += 1
            end += 1
        if min_length > len(s):
            return ''
        return s[substring_start: substring_start + min_length]
                    
                    
        