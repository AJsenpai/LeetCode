class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        start,end = 0,0
        result = []
        word_count = {}
        match = 0
        for char in p:
            if char not in word_count:
                word_count[char] = 0
            word_count[char] += 1
        
        while end<len(s):
            
            # calculation
            right_char = s[end]
            if right_char in word_count:
                word_count[right_char] -= 1            
                if word_count[right_char] == 0:
                    match += 1
            
            
            if (end-start+1) == len(p):
                # answer
                if match == len(word_count):
                    result.append(start)
                
                # before sliding widnow if the left_char
                # is a part of pattern put it back and recude the match
                left_char = s[start]
                if left_char in word_count:
                    if word_count[left_char] == 0:
                        match -= 1
                    
                    word_count[left_char] += 1
                start +=1
            end +=1
        return result
                