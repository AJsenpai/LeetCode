class Solution:
    def canJump(self, a: List[int]) -> bool:
        if len(a)==1:
            return True
        
        max_position = 0
        i = 0
        
        
        while i<=max_position:
            max_position = max(max_position, i + a[i])
            if max_position >= len(a)-1:
                return True
            i +=1
        return False
        
        