class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # other solution could be to use counter and create two hashmap

        for i in set(ransomNote):
            if ransomNote.count(i)>magazine.count(i):
                return False
        return True
                
        
        
        
        