class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        for n in nums:
            parsed_index = abs(n)-1
            if nums[parsed_index]>0:
                nums[parsed_index] *= -1
        
        return [i+1 for i,n in enumerate(nums) if n>0]
