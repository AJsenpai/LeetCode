class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # fixed size window
        
        start,end = 0,0
        hashmap = {}
        match = 0
        
        for char in s1:
            if char not in hashmap:
                hashmap[char] = 0
            hashmap[char] += 1
        
        while end<len(s2):
            right_char = s2[end]
            
            if right_char in hashmap:
                hashmap[right_char] -= 1
                if hashmap[right_char]==0:
                    match += 1
            
            if end-start+1 == len(s1):     
                if match == len(hashmap):
                    return True             
                
                left_char = s2[start]                
                if left_char in hashmap:
                    if hashmap[left_char]==0:
                        match -= 1
                    hashmap[left_char] += 1      
                start += 1
            end +=1
            

        return False
                
                