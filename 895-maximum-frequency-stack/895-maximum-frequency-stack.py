class FreqStack:

    def __init__(self):
        self.maxheap = []
        self.hashmap = {}
        self.count = 0

    def push(self, val: int) -> None:
        if val not in self.hashmap:
            self.hashmap[val] = 0
        self.hashmap[val]+=1          
        heappush(self.maxheap, (-self.hashmap[val], -self.count, val))        
        self.count += 1
        
        

    def pop(self) -> int:
        if self.maxheap:
            count, counter, num = heappop(self.maxheap)
            self.hashmap[num] -= 1

        return num
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()