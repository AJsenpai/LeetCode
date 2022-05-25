class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = {}
        for word in s:
            if word not in record:
                record[word] = 0
            record[word] += 1

        for word in t:
            if word not in record:
                return False
            else:
                record[word] -= 1       
        
        for i in record.values():
            if i!=0:
                return False
            
        return True

        # return all(x == 0 for x in record.values())    