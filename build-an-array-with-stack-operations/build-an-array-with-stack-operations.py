class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        index = 0
        for i in range(1,target[-1]+1): #**
            result.append('Push')
            if i != target[index]:
                result.append('Pop')
            else:
                index += 1
        return result
        