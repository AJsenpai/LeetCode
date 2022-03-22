class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        t = [False] * (len(s)+1)
        t[len(s)] = True
        
        for i in reversed(range(len(s))):
            for word in wordDict:
                if (i+len(word)) <=len(s) and s[i : i+len(word)] == word:
                    t[i] = t[i+len(word)]
                if t[i]:
                    break
        print(t)
        return t[0]
        
        