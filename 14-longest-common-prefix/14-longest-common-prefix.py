class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs,key=len)
        
        for i in range(len(shortest)):
            for others in strs:
            
            
                if others[i]!=shortest[i]:
                    return shortest[:i]
        return shortest
        