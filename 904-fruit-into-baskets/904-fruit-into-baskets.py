class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # same as longest substring with k distinct char here k = 2
        start,end = 0,0
        char_count = {}
        max_length = 0
        while end<len(fruits):
            right_char=  fruits[end]
            if right_char not in char_count:
                char_count[right_char] = 0
            char_count[right_char] += 1
            
            if len(char_count) <= 2:
                max_length = max(max_length, end-start+1)
            
            while len(char_count) > 2:
                left_char = fruits[start]
                char_count[left_char] -= 1
                if char_count[left_char] == 0:
                    del char_count[left_char]
                start += 1
            end += 1
        return max_length