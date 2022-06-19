class Solution:
    def greatestLetter(self, s: str) -> str:
        if s.isupper() or s.islower():
            return ''
        
        greatest = ''
        for char in s:
            if char.upper() in s and char.lower() in s:
                if char>greatest:
                    greatest=char
        return greatest.upper()
        
        