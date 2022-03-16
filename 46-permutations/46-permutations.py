class Solution:
    def permute(self, ip: List[int]) -> List[List[int]]:
        # decsion tree - every node gives the result
        # as we move down pop the element from start and add it again at the end
        
        result = []
        
        # base case
        if len(ip)==1:
            return [ip[:]]
            
        for  i in range(len(ip)):
            n = ip.pop(0)
            
            permutations = self.permute(ip) # recursive call
            
            # add back the popped number at the end
            for p in permutations:
                p.append(n)
            
            # add list of permutations to result
            result.extend(permutations)
            ip.append(n)
        return result
                