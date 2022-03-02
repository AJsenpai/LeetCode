class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool: 
        # using hashmap
        # track_num = {} # num:idx
        # for i,num in enumerate(nums):
        #     if num in track_num:
        #         return True
        #     track_num[num] = i
        # return False
        
        # pythonic solution
        return False if len(nums)== len(set(nums)) else True
        