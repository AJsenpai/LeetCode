class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord not in anagram:
                anagram[sortedWord] = []
            anagram[sortedWord].append(word)                            
        return list(anagram.values())
        