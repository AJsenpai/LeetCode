class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:

        for idx, word in enumerate(sentence.split()):
            if self.search_word(word, searchWord):
                return idx + 1
        return -1

    def search_word(self, word, searchWord):
        for i, w in enumerate(searchWord):
            if not (len(word) >= len(searchWord)) or (w != word[i]):
                return False
        return True