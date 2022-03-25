class Solution:
    def frequencySort(self, s: str) -> str:
        hashmap = {}
        for char in s:
            if char not in hashmap:
                hashmap[char] = 0
            hashmap[char]+=1
        
        maxheap = [] # sorting high to low
        
        for char,count in hashmap.items():
            heappush(maxheap,(-count,char))
        
        result = ''
        
        while maxheap:
            count,char = heappop(maxheap)
            
            for _ in range(-count):
                result+=char
        
        return result
        
        