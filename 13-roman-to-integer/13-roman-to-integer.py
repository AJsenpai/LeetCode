class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {'I':1,'V': 5,'X': 10 ,'L': 50,'C':100,'D':500,'M':1000}
        
        result= 0       
        # larger to smaller - add number
        # smaller before larger number - subtract smaller
        # Ex: IV, 1+5 = 6 but correct ans is 4. prev = 1, curr = 5
        # -1 + 5 = 4
        
        for i in range(len(s)):
            if i+1 < len(s) and hashmap[s[i]] < hashmap[s[i+1]]:
                result -= hashmap[s[i]]
            else:
                result += hashmap[s[i]]
        return result
                