class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # X + Y = Target
        # x, target-x
        
        hashmap = {}
        
        for idx, num in enumerate(nums):
            if target - num in hashmap:
                return hashmap[target-num], idx # Y, X            
            hashmap[num] = idx
        return -1
