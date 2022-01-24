class Solution:
    def capitalizeTitle(self, title: str) -> str:
        result = []
        for w in title.split():
            if len(w)>2:
                result.append(w.title())
            else:
                result.append(w.lower())
        
        return ' '.join(result)
        