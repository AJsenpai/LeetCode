class Solution:
    def totalFruit(self, a: List[int]) -> int:
        # same as longest substring with k distinct char here k = 2
        start,end = 0,0
        hashmap = {}
        max_length = 0
        
        while end < len(a):
            
            right_char = a[end]
            if right_char not in hashmap:
                hashmap[right_char]=0
            hashmap[right_char] += 1
            
            if len(hashmap)<=2: # ** <=
                max_length = max(max_length, end-start+1)
            
            if len(hashmap)>2:
                while len(hashmap)>2:
                    left_char = a[start]
                    hashmap[left_char] -= 1
                    
                    if hashmap[left_char]==0:
                        del hashmap[left_char]
                    start +=1
            end += 1
        return max_length
                        
