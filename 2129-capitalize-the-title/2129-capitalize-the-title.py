class Solution:
    def capitalizeTitle(self, title: str) -> str:
        result = ''
        for w in title.split():
            if len(w)>2:
                result += w.title()
            else:
                result += w.lower()
            result +=' '
        
        return result.strip()
        