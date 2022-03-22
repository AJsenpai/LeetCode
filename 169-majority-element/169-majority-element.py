class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count=1
        for i in range(1,len(nums)):
            if nums[i]==candidate:
                count += 1
            elif count>0:
                count -=1
            else: # count is 0
                candidate = nums[i]
                count = 1
        if nums.count(candidate)>len(nums)//2:
            return candidate
        