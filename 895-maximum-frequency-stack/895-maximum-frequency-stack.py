class FreqStack:

    def __init__(self):
        self.maxheap = []
        self.hashmap = {}
        self.idx = 0 # second priority if count is eqal

    def push(self, val: int) -> None:
        if val not in self.hashmap:
            self.hashmap[val] = 0
        self.hashmap[val]+=1          
        heappush(self.maxheap, (-self.hashmap[val], -self.idx, val))        
        self.idx += 1
        
        

    def pop(self) -> int:
        if self.maxheap:
            count, counter, num = heappop(self.maxheap)
            self.hashmap[num] -= 1

        return num
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()