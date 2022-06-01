class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # using xor
        result = 0
        for i in nums:
            result ^= i
        return result
        