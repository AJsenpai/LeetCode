class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words or len(words[0])==0:
            return []
        word_hashmap = {}
        result = []
        
        words_count = len(words)
        word_length = len(words[0])
        
        for word in words:
            if word not in word_hashmap:
                word_hashmap[word] = 0 
            word_hashmap[word] +=1
            
        for start in range((len(s) - words_count*word_length)+1):
            word_seen = {}
            
            for end in range(0,words_count):
                next_word_index = start + end * word_length
                word = s[next_word_index: next_word_index + word_length]
                
                if word not in word_hashmap:
                    break
                
                if word not in word_seen:
                    word_seen[word] = 0
                word_seen[word] += 1
                
                if word_seen[word] > word_hashmap[word]:
                    break
                
                if end + 1 == words_count:
                    result.append(start)
            
        
        return result
                
                
                
                
                
                
                
                
                
                