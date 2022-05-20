class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadanes Algorithm
        maxSoFar,maxEndingHere = nums[0],nums[0]
        for i in range(1,len(nums)):
            maxEndingHere = max(nums[i],nums[i]+maxEndingHere)
            maxSoFar = max(maxSoFar,maxEndingHere)
        return maxSoFar
        