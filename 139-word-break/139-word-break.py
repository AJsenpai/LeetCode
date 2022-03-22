class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # start from last and check if the word at index i
        # is matching length of word from wordDic is matching 
        # the current word or not
        # ex leetcode , i = 0 , word = 'leet' s[0:0+4] = leet --> matching
        t = [False] * (len(s)+1)
        t[len(s)] = True
        
        for i in reversed(range(len(s))):
            for word in wordDict:
                if (i+len(word)) <=len(s) and s[i : i+len(word)] == word:
                    t[i] = t[i+len(word)]
                if t[i]:
                    break

        return t[0]
        
        