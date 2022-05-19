import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        
        

    def reset(self) -> List[int]:        
        return self.nums
        

    def shuffle(self) -> List[int]:
        shuffle = self.nums[:]
        random.shuffle(shuffle)
        return shuffle
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()